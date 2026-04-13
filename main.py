# main.py — WOXHUB Community Bot (python-telegram-bot v20+)
# ═══════════════════════════════════════════════════════════════
#  Chạy: python main.py
#  Yêu cầu: pip install -r requirements.txt
#  Cấu hình: Copy .env.example → .env và điền thông tin
# ═══════════════════════════════════════════════════════════════
import logging
import re
import asyncio
import aiosqlite
from telegram import Update, ChatPermissions
from telegram.ext import (
    Application, CommandHandler, CallbackQueryHandler,
    MessageHandler, ChatMemberHandler, ContextTypes, filters,
)
from telegram.constants import ParseMode

import config
import database as db
import messages as msg
import keyboards as kb
import faq as faq_module
import scheduler as sched_module

logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

URL_PATTERN = re.compile(r"(https?://|www\.)\S+", re.IGNORECASE)

# Rate limiting: user_id → list of message timestamps
_rate_tracker: dict[int, list[float]] = {}


# ═══════════════════════════════════════════════════════════════
#  HELPERS
# ═══════════════════════════════════════════════════════════════

async def is_admin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> bool:
    user = update.effective_user
    if user.id in config.ADMIN_IDS:
        return True
    try:
        member = await context.bot.get_chat_member(config.GROUP_ID, user.id)
        return member.status in ("administrator", "creator")
    except Exception:
        return False


async def restrict_unverified(context, user_id: int):
    try:
        await context.bot.restrict_chat_member(
            chat_id=config.GROUP_ID, user_id=user_id,
            permissions=ChatPermissions(can_send_messages=False),
        )
    except Exception as e:
        logger.warning("Restrict failed for %s: %s", user_id, e)


async def unrestrict_member(context, user_id: int):
    try:
        await context.bot.restrict_chat_member(
            chat_id=config.GROUP_ID, user_id=user_id,
            permissions=ChatPermissions(
                can_send_messages=True,
                can_send_media_messages=True,
                can_send_other_messages=True,
                can_add_web_page_previews=True,
            ),
        )
    except Exception as e:
        logger.warning("Unrestrict failed for %s: %s", user_id, e)


def _check_rate_limit(user_id: int) -> bool:
    """True nếu user vượt rate limit (spam)."""
    import time
    now = time.time()
    window = config.RATE_LIMIT_WINDOW
    limit = config.RATE_LIMIT_MESSAGES
    history = _rate_tracker.get(user_id, [])
    history = [t for t in history if now - t < window]
    history.append(now)
    _rate_tracker[user_id] = history
    return len(history) > limit


# ═══════════════════════════════════════════════════════════════
#  USER COMMANDS
# ═══════════════════════════════════════════════════════════════

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    args = context.args
    ref_id = None

    if args and args[0].startswith("REF_"):
        ref_username = args[0][4:]
        async with aiosqlite.connect(db.DB_PATH) as conn:
            async with conn.execute(
                "SELECT user_id FROM members WHERE username = ?", (ref_username,)
            ) as cur:
                row = await cur.fetchone()
                if row:
                    ref_id = row[0]

    await db.upsert_member(user.id, user.username or "", user.full_name, ref_id)

    if ref_id and ref_id != user.id:
        await db.add_referral(referrer_id=ref_id, referee_id=user.id)
        await db.add_score(ref_id, "referral_made")

    await update.message.reply_text(
        msg.start_message(user.first_name),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=kb.main_menu_keyboard(),
    )


async def rules_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    verified = await db.is_verified(user.id)
    await update.message.reply_text(
        msg.NOI_QUY,
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=kb.noi_quy_keyboard(verified=verified),
    )


async def myref_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    ref_count = await db.count_referrals(user.id)
    score = await db.get_score(user.id)
    await update.message.reply_text(
        msg.my_referral_message(user.username or "", ref_count, score, config.BOT_USERNAME),
        parse_mode=ParseMode.MARKDOWN,
    )


async def score_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    score = await db.get_score(user.id)
    ref_count = await db.count_referrals(user.id)
    await update.message.reply_text(
        msg.score_message(user.full_name, score, ref_count),
        parse_mode=ParseMode.MARKDOWN,
    )


async def faq_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "❓ *CÂU HỎI THƯỜNG GẶP — WOXHUB*\n\nChọn câu hỏi bạn muốn được giải đáp:",
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=kb.faq_menu_keyboard(),
    )


# ═══════════════════════════════════════════════════════════════
#  ADMIN COMMANDS
# ═══════════════════════════════════════════════════════════════

async def stats_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await is_admin(update, context):
        await update.message.reply_text("⛔ Lệnh này chỉ dành cho admin.")
        return
    total = await db.get_total_members()
    top_refs = await db.get_top_referrers()
    signal_count = await db.get_signal_count(7)
    await update.message.reply_text(
        msg.admin_stats_message(total, top_refs, signal_count),
        parse_mode=ParseMode.MARKDOWN,
    )


async def getid_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    user = update.effective_user
    await update.message.reply_text(
        f"💬 *Chat Info:*\n"
        f"ID: `{chat.id}`\nType: {chat.type}\nTitle: {chat.title or 'N/A'}\n\n"
        f"👤 *Your Info:*\nUser ID: `{user.id}`\nUsername: @{user.username}",
        parse_mode=ParseMode.MARKDOWN,
    )


async def warn_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await is_admin(update, context):
        return
    if not update.message.reply_to_message:
        await update.message.reply_text("↩️ Reply vào tin nhắn cần warn.")
        return
    target = update.message.reply_to_message.from_user
    reason = " ".join(context.args) if context.args else "Vi phạm luật nhóm"
    count = await db.add_warning(target.id, reason)
    await update.message.reply_text(
        msg.spam_warning_message(target.full_name, count, config.MAX_WARNINGS),
        parse_mode=ParseMode.MARKDOWN,
    )
    if count >= config.MAX_WARNINGS:
        try:
            await context.bot.ban_chat_member(config.GROUP_ID, target.id)
            await update.message.reply_text(msg.KICKED_MESSAGE)
            await db.reset_warnings(target.id)
        except Exception as e:
            logger.error("Kick failed for %s: %s", target.id, e)


async def unwarn_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await is_admin(update, context):
        return
    if not update.message.reply_to_message:
        await update.message.reply_text("↩️ Reply vào người cần xóa cảnh cáo.")
        return
    target = update.message.reply_to_message.from_user
    await db.reset_warnings(target.id)
    await update.message.reply_text(f"✅ Đã xóa toàn bộ cảnh cáo cho {target.full_name}.")


async def mute_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await is_admin(update, context):
        return
    if not update.message.reply_to_message:
        await update.message.reply_text("↩️ Reply vào người cần mute. Dùng: /mute <phút>")
        return
    target = update.message.reply_to_message.from_user
    minutes = int(context.args[0]) if context.args and context.args[0].isdigit() else 60
    until = update.message.date.timestamp() + minutes * 60
    try:
        await context.bot.restrict_chat_member(
            config.GROUP_ID, target.id,
            permissions=ChatPermissions(can_send_messages=False),
            until_date=int(until),
        )
        await update.message.reply_text(f"🔇 {target.full_name} bị mute {minutes} phút.")
    except Exception as e:
        await update.message.reply_text(f"Lỗi: {e}")


async def ban_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await is_admin(update, context):
        return
    if not update.message.reply_to_message:
        await update.message.reply_text("↩️ Reply vào người cần ban.")
        return
    target = update.message.reply_to_message.from_user
    reason = " ".join(context.args) if context.args else "Vi phạm nghiêm trọng"
    try:
        await context.bot.ban_chat_member(config.GROUP_ID, target.id)
        await update.message.reply_text(f"⛔ {target.full_name} đã bị ban.\nLý do: {reason}")
    except Exception as e:
        await update.message.reply_text(f"Lỗi: {e}")


async def warn_list_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await is_admin(update, context):
        return
    warned = await db.get_warned_members()
    if not warned:
        await update.message.reply_text("✅ Không có thành viên nào đang bị cảnh cáo.")
        return
    text = "⚠️ *DANH SÁCH ĐANG BỊ CẢNH CÁO:*\n━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
    for m in warned:
        name = m.get("full_name") or m.get("username") or str(m["user_id"])
        text += f"• {name} — *{m['warn_count']}/3* lần\n"
    await update.message.reply_text(text, parse_mode=ParseMode.MARKDOWN)


async def broadcast_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await is_admin(update, context):
        return
    if not context.args:
        await update.message.reply_text("Dùng: /broadcast <tin nhắn>")
        return
    text = " ".join(context.args)
    member_ids = await db.get_all_member_ids()
    success, fail = 0, 0
    await update.message.reply_text(f"📢 Đang gửi tới {len(member_ids)} thành viên...")
    for uid in member_ids:
        try:
            await context.bot.send_message(uid, f"📢 *THÔNG BÁO TỪ WOXHUB:*\n\n{text}",
                                           parse_mode=ParseMode.MARKDOWN)
            success += 1
            await asyncio.sleep(0.05)  # 20 msg/s max
        except Exception:
            fail += 1
    await update.message.reply_text(f"✅ Gửi thành công: {success} | ❌ Thất bại: {fail}")


async def seed_now_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await is_admin(update, context):
        return
    if not context.args:
        jobs = ", ".join(sched_module.JOB_MAP.keys())
        await update.message.reply_text(f"Dùng: /seed_now <job_name>\nCác job: {jobs}")
        return
    job_name = context.args[0]
    job_fn = sched_module.JOB_MAP.get(job_name)
    if not job_fn:
        await update.message.reply_text(f"❌ Không tìm thấy job '{job_name}'")
        return
    await update.message.reply_text(f"▶️ Đang chạy job: {job_name}...")
    await job_fn(context)
    await update.message.reply_text(f"✅ Job '{job_name}' đã chạy xong.")


async def reload_faq_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await is_admin(update, context):
        return
    rules = faq_module.load_faq_rules()
    await update.message.reply_text(f"✅ Đã reload FAQ: {len(rules)} rules.")


async def signal_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Admin tự gửi tín hiệu thủ công: /signal <nội dung>"""
    if not await is_admin(update, context):
        return
    if not context.args:
        await update.message.reply_text("Dùng: /signal <nội dung tín hiệu>")
        return
    signal_text = " ".join(context.args)
    formatted = msg.format_signal_message(signal_text)
    await context.bot.send_message(
        config.GROUP_ID,
        formatted,
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=kb.signal_keyboard(config.BROKER_LINK_PUPRIME),
    )
    await db.log_signal(0, 0, signal_text[:200])
    await update.message.reply_text("✅ Tín hiệu đã được gửi vào nhóm.")


async def export_leads_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await is_admin(update, context):
        return
    members = await db.get_high_score_members(50)
    if not members:
        await update.message.reply_text("Chưa có lead nào đạt 50 điểm.")
        return
    lines = ["user_id,username,full_name,score,warn_count"]
    for m in members:
        lines.append(f"{m['user_id']},{m.get('username','')},{m.get('full_name','')},{m['score']},{m['warn_count']}")
    csv_text = "\n".join(lines)
    # Gửi dạng file text
    import io
    buf = io.BytesIO(csv_text.encode("utf-8"))
    buf.name = "woxhub_leads.csv"
    await context.bot.send_document(
        update.effective_chat.id,
        document=buf,
        caption=f"📊 {len(members)} leads với score ≥ 50",
    )


async def faq_stats_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await is_admin(update, context):
        return
    stats = await db.get_faq_stats(10)
    if not stats:
        await update.message.reply_text("Chưa có dữ liệu FAQ.")
        return
    text = "📊 *TOP FAQ KEYWORDS:*\n━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
    for i, s in enumerate(stats, 1):
        text += f"{i}. `{s['matched_keyword']}` — {s['hits']} lần\n"
    await update.message.reply_text(text, parse_mode=ParseMode.MARKDOWN)


# ═══════════════════════════════════════════════════════════════
#  NEW MEMBER JOIN
# ═══════════════════════════════════════════════════════════════

async def on_new_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = update.chat_member
    if result.new_chat_member.status not in ("member", "restricted"):
        return
    if result.old_chat_member.status in ("member", "administrator", "creator", "restricted"):
        return

    user = result.new_chat_member.user
    if user.is_bot:
        return

    await db.upsert_member(user.id, user.username or "", user.full_name)
    await restrict_unverified(context, user.id)

    # Gửi welcome vào nhóm
    await context.bot.send_message(
        chat_id=config.GROUP_ID,
        text=msg.welcome_new_member(user.first_name),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=kb.welcome_keyboard(),
    )

    # Thử gửi DM với nội quy đầy đủ
    try:
        await context.bot.send_message(
            chat_id=user.id,
            text=msg.NOI_QUY,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=kb.verify_keyboard(),
        )
    except Exception:
        logger.info("Cannot DM user %s", user.id)


# ═══════════════════════════════════════════════════════════════
#  SIGNAL CHANNEL FORWARDING
# ═══════════════════════════════════════════════════════════════

async def signal_channel_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Nhận tin từ WOXBOT SIGNAL channel và forward vào nhóm WOXHUB.
    Bot phải là member của channel đó.
    """
    if not config.SIGNAL_ENABLED:
        return

    message = update.channel_post or update.message
    if not message:
        return

    text = message.text or message.caption or ""
    if not text:
        return

    formatted = msg.format_signal_message(text)
    try:
        await context.bot.send_message(
            config.GROUP_ID,
            formatted,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=kb.signal_keyboard(config.BROKER_LINK_PUPRIME),
        )
        await db.log_signal(message.message_id, message.chat.id, text[:200])
        logger.info("Signal forwarded from channel")
    except Exception as e:
        logger.error("Signal forward failed: %s", e)


# ═══════════════════════════════════════════════════════════════
#  CALLBACK QUERY ROUTER
# ═══════════════════════════════════════════════════════════════

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user = query.from_user
    data = query.data
    await query.answer()
    await db.upsert_member(user.id, user.username or "", user.full_name)

    # ── Main menu ──────────────────────────────────────────────
    if data == "main_menu":
        await query.edit_message_text(
            msg.start_message(user.first_name),
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=kb.main_menu_keyboard(),
        )

    # ── Xác nhận nội quy ──────────────────────────────────────
    elif data == "verify_member":
        if await db.is_verified(user.id):
            await query.answer("✅ Bạn đã xác nhận rồi!", show_alert=True)
            return
        await db.set_verified(user.id)
        await db.add_score(user.id, "verified")
        await unrestrict_member(context, user.id)
        await query.edit_message_text(
            msg.VERIFICATION_SUCCESS,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=kb.main_menu_keyboard(),
        )

    # ── Nội quy ───────────────────────────────────────────────
    elif data == "noi_quy":
        verified = await db.is_verified(user.id)
        await query.edit_message_text(
            msg.NOI_QUY,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=kb.noi_quy_keyboard(verified=verified),
        )

    # ── Quyền lợi & phần thưởng ───────────────────────────────
    elif data == "quyen_loi":
        await db.add_score(user.id, "view_rewards")
        await query.edit_message_text(
            msg.QUYEN_LOI,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=kb.quyen_loi_keyboard(),
        )

    # ── Đăng ký sàn ───────────────────────────────────────────
    elif data == "dang_ky_san":
        await db.add_score(user.id, "click_broker")
        await query.edit_message_text(
            msg.dang_ky_san_message(config.BROKER_LINK_PUPRIME, config.BROKER_LINK_TOMO, config.BROKER_LINK_DBG),
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=kb.dang_ky_san_keyboard(
                config.BROKER_LINK_PUPRIME,
                config.BROKER_LINK_TOMO,
                config.BROKER_LINK_DBG,
                config.ADMIN_USERNAME,
            ),
        )

    # ── Dự án WOXBAL ──────────────────────────────────────────
    elif data == "woxbal_projects":
        await query.edit_message_text(
            msg.WOXBAL_PROJECT_INTRO,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=kb.woxbal_projects_keyboard(),
        )

    elif data == "project_woxbot":
        await db.add_score(user.id, "view_woxbot")
        await query.edit_message_text(
            msg.WOXBOT_INFO,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=kb.back_to_projects_keyboard(),
        )

    elif data == "project_woxbiz":
        await db.add_score(user.id, "view_woxbiz")
        await query.edit_message_text(
            msg.WOXBIZ_INFO,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=kb.back_to_projects_keyboard(),
        )

    elif data == "project_woxdemy":
        await db.add_score(user.id, "view_woxdemy")
        await query.edit_message_text(
            msg.WOXDEMY_INFO,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=kb.back_to_projects_keyboard(),
        )

    # ── FAQ Menu ──────────────────────────────────────────────
    elif data == "faq_menu":
        await query.edit_message_text(
            "❓ *CÂU HỎI THƯỜNG GẶP — WOXHUB*\n\nChọn câu hỏi bạn muốn được giải đáp:",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=kb.faq_menu_keyboard(),
        )

    elif data.startswith("faq_"):
        await faq_module.faq_quick_reply(query, context)

    # ── My Ref ────────────────────────────────────────────────
    elif data == "my_ref":
        ref_count = await db.count_referrals(user.id)
        score = await db.get_score(user.id)
        await query.edit_message_text(
            msg.my_referral_message(
                user.username or "", ref_count, score, config.BOT_USERNAME
            ),
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=kb.back_to_main_keyboard(),
        )

    # ── Support ───────────────────────────────────────────────
    elif data == "support":
        await query.edit_message_text(
            msg.support_message(config.ADMIN_USERNAME),
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=kb.support_keyboard(config.ADMIN_USERNAME),
        )


# ═══════════════════════════════════════════════════════════════
#  ANTI-SPAM
# ═══════════════════════════════════════════════════════════════

async def anti_spam_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    if not message or not message.text:
        return
    if message.chat.id != config.GROUP_ID:
        return
    user = message.from_user
    if user.id in config.ADMIN_IDS:
        return

    # Lead scoring: câu hỏi về giá/sản phẩm
    price_kw = ["giá", "price", "bao nhiêu", "spread", "lot", "xauusd", "vàng", "gold"]
    if any(kw in message.text.lower() for kw in price_kw):
        await db.add_score(user.id, "ask_price")

    # Rate limiting
    if _check_rate_limit(user.id):
        try:
            await context.bot.restrict_chat_member(
                config.GROUP_ID, user.id,
                permissions=ChatPermissions(can_send_messages=False),
                until_date=int(message.date.timestamp()) + 1800,  # mute 30 phút
            )
            await context.bot.send_message(
                config.GROUP_ID,
                f"⏸️ {user.full_name} đã bị mute 30 phút do gửi tin quá nhanh.",
            )
        except Exception:
            pass
        return

    # Xóa link ngoài
    if URL_PATTERN.search(message.text):
        try:
            await message.delete()
        except Exception:
            return
        count = await db.add_warning(user.id, "Spam link ngoài")
        await context.bot.send_message(
            chat_id=config.GROUP_ID,
            text=msg.spam_warning_message(user.full_name, count, config.MAX_WARNINGS),
            parse_mode=ParseMode.MARKDOWN,
        )
        if count >= config.MAX_WARNINGS:
            try:
                await context.bot.ban_chat_member(config.GROUP_ID, user.id)
                await context.bot.send_message(config.GROUP_ID, msg.KICKED_MESSAGE)
                await db.reset_warnings(user.id)
            except Exception as e:
                logger.error("Kick failed: %s", e)


# ═══════════════════════════════════════════════════════════════
#  APP SETUP
# ═══════════════════════════════════════════════════════════════

async def post_init(application: Application):
    await db.init_db()
    faq_module.load_faq_rules()
    sched_module.setup_scheduler(application)
    logger.info("✅ WOXHUB Bot started — DB & Scheduler ready.")


def main():
    application = (
        Application.builder()
        .token(config.BOT_TOKEN)
        .post_init(post_init)
        .build()
    )

    # ── User commands ──────────────────────────────────────────
    application.add_handler(CommandHandler(["start", "menu"], start))
    application.add_handler(CommandHandler("rules", rules_command))
    application.add_handler(CommandHandler("myref", myref_command))
    application.add_handler(CommandHandler("score", score_command))
    application.add_handler(CommandHandler("faq", faq_command))

    # ── Admin commands ─────────────────────────────────────────
    application.add_handler(CommandHandler("stats", stats_command))
    application.add_handler(CommandHandler("getid", getid_command))
    application.add_handler(CommandHandler("warn", warn_command))
    application.add_handler(CommandHandler("unwarn", unwarn_command))
    application.add_handler(CommandHandler("mute", mute_command))
    application.add_handler(CommandHandler("ban", ban_command))
    application.add_handler(CommandHandler("warn_list", warn_list_command))
    application.add_handler(CommandHandler("broadcast", broadcast_command))
    application.add_handler(CommandHandler("seed_now", seed_now_command))
    application.add_handler(CommandHandler("reload_faq", reload_faq_command))
    application.add_handler(CommandHandler("signal", signal_command))
    application.add_handler(CommandHandler("export_leads", export_leads_command))
    application.add_handler(CommandHandler("faq_stats", faq_stats_command))

    # ── Callbacks ──────────────────────────────────────────────
    application.add_handler(CallbackQueryHandler(button_callback))

    # ── New member handler ─────────────────────────────────────
    application.add_handler(
        ChatMemberHandler(on_new_member, ChatMemberHandler.CHAT_MEMBER)
    )

    # ── Signal channel handler (priority group=0) ──────────────
    if config.SIGNAL_CHANNEL_ID != 0:
        application.add_handler(
            MessageHandler(
                filters.Chat(config.SIGNAL_CHANNEL_ID),
                signal_channel_handler,
            ),
            group=0,
        )

    # ── FAQ auto-reply (group=1) ───────────────────────────────
    application.add_handler(
        MessageHandler(
            filters.TEXT & filters.Chat(config.GROUP_ID) & ~filters.COMMAND,
            faq_module.faq_message_handler,
        ),
        group=1,
    )

    # ── Anti-spam (group=2) ────────────────────────────────────
    application.add_handler(
        MessageHandler(
            filters.TEXT & filters.Chat(config.GROUP_ID) & ~filters.COMMAND,
            anti_spam_handler,
        ),
        group=2,
    )

    logger.info("🚀 WOXHUB Community Bot is running...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
