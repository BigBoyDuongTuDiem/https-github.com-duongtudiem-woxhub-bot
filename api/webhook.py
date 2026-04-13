# api/webhook.py — Vercel Serverless Webhook Handler for WOXHUB Bot
import sys, os, json, asyncio, re
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from http.server import BaseHTTPRequestHandler
from telegram import Update, ChatPermissions
from telegram.ext import (
    Application, CommandHandler, CallbackQueryHandler,
    MessageHandler, ChatMemberHandler, filters,
)
from telegram.constants import ParseMode
import aiosqlite

import config
import database as db
import messages as msg
import keyboards as kb
import faq as faq_module

URL_PATTERN = re.compile(r"(https?://|www\.)\S+", re.IGNORECASE)


# ── Build Application (singleton per cold start) ──────────────────────────────
_application = None

async def get_application():
    global _application
    if _application is not None:
        return _application

    app = Application.builder().token(config.BOT_TOKEN).build()

    # User commands
    app.add_handler(CommandHandler(["start", "menu"], _start))
    app.add_handler(CommandHandler("rules",   _rules))
    app.add_handler(CommandHandler("myref",   _myref))
    app.add_handler(CommandHandler("score",   _score))
    app.add_handler(CommandHandler("faq",     _faq_cmd))

    # Admin commands
    app.add_handler(CommandHandler("stats",        _stats))
    app.add_handler(CommandHandler("getid",        _getid))
    app.add_handler(CommandHandler("warn",         _warn))
    app.add_handler(CommandHandler("unwarn",       _unwarn))
    app.add_handler(CommandHandler("mute",         _mute))
    app.add_handler(CommandHandler("ban",          _ban))
    app.add_handler(CommandHandler("warn_list",    _warn_list))
    app.add_handler(CommandHandler("signal",       _signal_cmd))
    app.add_handler(CommandHandler("reload_faq",   _reload_faq))

    # Callbacks
    app.add_handler(CallbackQueryHandler(_button_callback))

    # New member
    app.add_handler(ChatMemberHandler(_on_new_member, ChatMemberHandler.CHAT_MEMBER))

    # FAQ auto-reply (group=1)
    app.add_handler(MessageHandler(
        filters.TEXT & filters.Chat(config.GROUP_ID) & ~filters.COMMAND,
        faq_module.faq_message_handler,
    ), group=1)

    # Anti-spam (group=2)
    app.add_handler(MessageHandler(
        filters.TEXT & filters.Chat(config.GROUP_ID) & ~filters.COMMAND,
        _anti_spam,
    ), group=2)

    # Signal channel forwarding
    if config.SIGNAL_CHANNEL_ID != 0:
        app.add_handler(MessageHandler(
            filters.Chat(config.SIGNAL_CHANNEL_ID),
            _signal_forward,
        ), group=0)

    await db.init_db()
    faq_module.load_faq_rules()
    await app.initialize()
    _application = app
    return app


# ── Helpers ───────────────────────────────────────────────────────────────────

async def _is_admin(update, context):
    user = update.effective_user
    if user.id in config.ADMIN_IDS:
        return True
    try:
        m = await context.bot.get_chat_member(config.GROUP_ID, user.id)
        return m.status in ("administrator", "creator")
    except Exception:
        return False

async def _restrict(context, user_id):
    try:
        await context.bot.restrict_chat_member(
            config.GROUP_ID, user_id,
            permissions=ChatPermissions(can_send_messages=False))
    except Exception:
        pass

async def _unrestrict(context, user_id):
    try:
        await context.bot.restrict_chat_member(
            config.GROUP_ID, user_id,
            permissions=ChatPermissions(
                can_send_messages=True, can_send_media_messages=True,
                can_send_other_messages=True, can_add_web_page_previews=True))
    except Exception:
        pass


# ── User Handlers ─────────────────────────────────────────────────────────────

async def _start(update, context):
    user = update.effective_user
    args = context.args
    ref_id = None
    if args and args[0].startswith("REF_"):
        ref_username = args[0][4:]
        async with aiosqlite.connect(db.DB_PATH) as conn:
            async with conn.execute("SELECT user_id FROM members WHERE username=?", (ref_username,)) as cur:
                row = await cur.fetchone()
                if row: ref_id = row[0]
    await db.upsert_member(user.id, user.username or "", user.full_name, ref_id)
    if ref_id and ref_id != user.id:
        await db.add_referral(referrer_id=ref_id, referee_id=user.id)
        await db.add_score(ref_id, "referral_made")
    await update.message.reply_text(msg.start_message(user.first_name),
        parse_mode=ParseMode.MARKDOWN, reply_markup=kb.main_menu_keyboard())

async def _rules(update, context):
    user = update.effective_user
    verified = await db.is_verified(user.id)
    await update.message.reply_text(msg.NOI_QUY, parse_mode=ParseMode.MARKDOWN,
        reply_markup=kb.noi_quy_keyboard(verified=verified))

async def _myref(update, context):
    user = update.effective_user
    await update.message.reply_text(
        msg.my_referral_message(user.username or "", await db.count_referrals(user.id),
                                 await db.get_score(user.id), config.BOT_USERNAME),
        parse_mode=ParseMode.MARKDOWN)

async def _score(update, context):
    user = update.effective_user
    await update.message.reply_text(
        msg.score_message(user.full_name, await db.get_score(user.id), await db.count_referrals(user.id)),
        parse_mode=ParseMode.MARKDOWN)

async def _faq_cmd(update, context):
    await update.message.reply_text(
        "❓ *CÂU HỎI THƯỜNG GẶP — WOXHUB*\n\nChọn câu hỏi bạn muốn được giải đáp:",
        parse_mode=ParseMode.MARKDOWN, reply_markup=kb.faq_menu_keyboard())


# ── Admin Handlers ────────────────────────────────────────────────────────────

async def _stats(update, context):
    if not await _is_admin(update, context):
        return
    total = await db.get_total_members()
    top_refs = await db.get_top_referrers()
    signal_count = await db.get_signal_count(7)
    await update.message.reply_text(
        msg.admin_stats_message(total, top_refs, signal_count), parse_mode=ParseMode.MARKDOWN)

async def _getid(update, context):
    chat = update.effective_chat
    user = update.effective_user
    await update.message.reply_text(
        f"💬 *Chat:* `{chat.id}` ({chat.type})\n👤 *You:* `{user.id}` @{user.username}",
        parse_mode=ParseMode.MARKDOWN)

async def _warn(update, context):
    if not await _is_admin(update, context): return
    if not update.message.reply_to_message:
        await update.message.reply_text("↩️ Reply vào tin nhắn cần warn."); return
    target = update.message.reply_to_message.from_user
    reason = " ".join(context.args) if context.args else "Vi phạm luật nhóm"
    count = await db.add_warning(target.id, reason)
    await update.message.reply_text(
        msg.spam_warning_message(target.full_name, count, config.MAX_WARNINGS), parse_mode=ParseMode.MARKDOWN)
    if count >= config.MAX_WARNINGS:
        try:
            await context.bot.ban_chat_member(config.GROUP_ID, target.id)
            await update.message.reply_text(msg.KICKED_MESSAGE)
            await db.reset_warnings(target.id)
        except Exception: pass

async def _unwarn(update, context):
    if not await _is_admin(update, context): return
    if not update.message.reply_to_message:
        await update.message.reply_text("↩️ Reply vào người cần xóa cảnh cáo."); return
    target = update.message.reply_to_message.from_user
    await db.reset_warnings(target.id)
    await update.message.reply_text(f"✅ Đã xóa cảnh cáo cho {target.full_name}.")

async def _mute(update, context):
    if not await _is_admin(update, context): return
    if not update.message.reply_to_message:
        await update.message.reply_text("↩️ Reply vào người cần mute. /mute <phút>"); return
    target = update.message.reply_to_message.from_user
    minutes = int(context.args[0]) if context.args and context.args[0].isdigit() else 60
    until = int(update.message.date.timestamp()) + minutes * 60
    try:
        await context.bot.restrict_chat_member(
            config.GROUP_ID, target.id,
            permissions=ChatPermissions(can_send_messages=False), until_date=until)
        await update.message.reply_text(f"🔇 {target.full_name} bị mute {minutes} phút.")
    except Exception as e:
        await update.message.reply_text(f"Lỗi: {e}")

async def _ban(update, context):
    if not await _is_admin(update, context): return
    if not update.message.reply_to_message:
        await update.message.reply_text("↩️ Reply vào người cần ban."); return
    target = update.message.reply_to_message.from_user
    reason = " ".join(context.args) if context.args else "Vi phạm nghiêm trọng"
    try:
        await context.bot.ban_chat_member(config.GROUP_ID, target.id)
        await update.message.reply_text(f"⛔ {target.full_name} đã bị ban.\nLý do: {reason}")
    except Exception as e:
        await update.message.reply_text(f"Lỗi: {e}")

async def _warn_list(update, context):
    if not await _is_admin(update, context): return
    warned = await db.get_warned_members()
    if not warned:
        await update.message.reply_text("✅ Không có thành viên nào đang bị cảnh cáo."); return
    text = "⚠️ *ĐANG BỊ CẢNH CÁO:*\n\n"
    for m in warned:
        name = m.get("full_name") or m.get("username") or str(m["user_id"])
        text += f"• {name} — *{m['warn_count']}/3*\n"
    await update.message.reply_text(text, parse_mode=ParseMode.MARKDOWN)

async def _signal_cmd(update, context):
    if not await _is_admin(update, context): return
    if not context.args:
        await update.message.reply_text("Dùng: /signal <nội dung>"); return
    signal_text = " ".join(context.args)
    formatted = msg.format_signal_message(signal_text)
    await context.bot.send_message(config.GROUP_ID, formatted,
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=kb.signal_keyboard(config.BROKER_LINK_PUPRIME))
    await db.log_signal(0, 0, signal_text[:200])
    await update.message.reply_text("✅ Tín hiệu đã gửi vào nhóm.")

async def _reload_faq(update, context):
    if not await _is_admin(update, context): return
    rules = faq_module.load_faq_rules()
    await update.message.reply_text(f"✅ Đã reload FAQ: {len(rules)} rules.")


# ── New Member ────────────────────────────────────────────────────────────────

async def _on_new_member(update, context):
    result = update.chat_member
    if result.new_chat_member.status not in ("member", "restricted"):
        return
    if result.old_chat_member.status in ("member", "administrator", "creator", "restricted"):
        return
    user = result.new_chat_member.user
    if user.is_bot:
        return
    await db.upsert_member(user.id, user.username or "", user.full_name)
    await _restrict(context, user.id)
    await context.bot.send_message(config.GROUP_ID,
        msg.welcome_new_member(user.first_name),
        parse_mode=ParseMode.MARKDOWN, reply_markup=kb.welcome_keyboard())
    try:
        await context.bot.send_message(user.id, msg.NOI_QUY,
            parse_mode=ParseMode.MARKDOWN, reply_markup=kb.verify_keyboard())
    except Exception:
        pass


# ── Signal Forward ────────────────────────────────────────────────────────────

async def _signal_forward(update, context):
    if not config.SIGNAL_ENABLED: return
    message = update.channel_post or update.message
    if not message: return
    text = message.text or message.caption or ""
    if not text: return
    formatted = msg.format_signal_message(text)
    try:
        await context.bot.send_message(config.GROUP_ID, formatted,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=kb.signal_keyboard(config.BROKER_LINK_PUPRIME))
        await db.log_signal(message.message_id, message.chat.id, text[:200])
    except Exception as e:
        print(f"Signal forward error: {e}")


# ── Callback Router ───────────────────────────────────────────────────────────

async def _button_callback(update, context):
    query = update.callback_query
    user  = query.from_user
    data  = query.data
    await query.answer()
    await db.upsert_member(user.id, user.username or "", user.full_name)

    if data == "main_menu":
        await query.edit_message_text(msg.start_message(user.first_name),
            parse_mode=ParseMode.MARKDOWN, reply_markup=kb.main_menu_keyboard())

    elif data == "verify_member":
        if await db.is_verified(user.id):
            await query.answer("✅ Bạn đã xác nhận rồi!", show_alert=True); return
        await db.set_verified(user.id)
        await db.add_score(user.id, "verified")
        await _unrestrict(context, user.id)
        await query.edit_message_text(msg.VERIFICATION_SUCCESS,
            parse_mode=ParseMode.MARKDOWN, reply_markup=kb.main_menu_keyboard())

    elif data == "noi_quy":
        verified = await db.is_verified(user.id)
        await query.edit_message_text(msg.NOI_QUY, parse_mode=ParseMode.MARKDOWN,
            reply_markup=kb.noi_quy_keyboard(verified=verified))

    elif data == "quyen_loi":
        await db.add_score(user.id, "view_rewards")
        await query.edit_message_text(msg.QUYEN_LOI, parse_mode=ParseMode.MARKDOWN,
            reply_markup=kb.quyen_loi_keyboard())

    elif data == "dang_ky_san":
        await db.add_score(user.id, "click_broker")
        await query.edit_message_text(
            msg.dang_ky_san_message(config.BROKER_LINK_PUPRIME, config.BROKER_LINK_TOMO, config.BROKER_LINK_DBG),
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=kb.dang_ky_san_keyboard(
                config.BROKER_LINK_PUPRIME, config.BROKER_LINK_TOMO,
                config.BROKER_LINK_DBG, config.ADMIN_USERNAME))

    elif data == "woxbal_projects":
        await query.edit_message_text(msg.WOXBAL_PROJECT_INTRO,
            parse_mode=ParseMode.MARKDOWN, reply_markup=kb.woxbal_projects_keyboard())

    elif data == "project_woxbot":
        await db.add_score(user.id, "view_woxbot")
        await query.edit_message_text(msg.WOXBOT_INFO, parse_mode=ParseMode.MARKDOWN,
            reply_markup=kb.back_to_projects_keyboard())

    elif data == "project_woxbiz":
        await db.add_score(user.id, "view_woxbiz")
        await query.edit_message_text(msg.WOXBIZ_INFO, parse_mode=ParseMode.MARKDOWN,
            reply_markup=kb.back_to_projects_keyboard())

    elif data == "project_woxdemy":
        await db.add_score(user.id, "view_woxdemy")
        await query.edit_message_text(msg.WOXDEMY_INFO, parse_mode=ParseMode.MARKDOWN,
            reply_markup=kb.back_to_projects_keyboard())

    elif data == "faq_menu":
        await query.edit_message_text(
            "❓ *CÂU HỎI THƯỜNG GẶP — WOXHUB*\n\nChọn câu hỏi bạn muốn được giải đáp:",
            parse_mode=ParseMode.MARKDOWN, reply_markup=kb.faq_menu_keyboard())

    elif data.startswith("faq_"):
        await faq_module.faq_quick_reply(query, context)

    elif data == "my_ref":
        await query.edit_message_text(
            msg.my_referral_message(user.username or "", await db.count_referrals(user.id),
                                     await db.get_score(user.id), config.BOT_USERNAME),
            parse_mode=ParseMode.MARKDOWN, reply_markup=kb.back_to_main_keyboard())

    elif data == "support":
        await query.edit_message_text(msg.support_message(config.ADMIN_USERNAME),
            parse_mode=ParseMode.MARKDOWN, reply_markup=kb.support_keyboard(config.ADMIN_USERNAME))


# ── Anti-Spam ─────────────────────────────────────────────────────────────────

async def _anti_spam(update, context):
    message = update.message
    if not message or not message.text: return
    if message.chat.id != config.GROUP_ID: return
    user = message.from_user
    if user.id in config.ADMIN_IDS: return
    price_kw = ["giá", "price", "bao nhiêu", "spread", "lot", "xauusd", "vàng", "gold"]
    if any(kw in message.text.lower() for kw in price_kw):
        await db.add_score(user.id, "ask_price")
    if URL_PATTERN.search(message.text):
        try: await message.delete()
        except Exception: return
        count = await db.add_warning(user.id, "Spam link ngoài")
        await context.bot.send_message(config.GROUP_ID,
            msg.spam_warning_message(user.full_name, count, config.MAX_WARNINGS),
            parse_mode=ParseMode.MARKDOWN)
        if count >= config.MAX_WARNINGS:
            try:
                await context.bot.ban_chat_member(config.GROUP_ID, user.id)
                await context.bot.send_message(config.GROUP_ID, msg.KICKED_MESSAGE)
                await db.reset_warnings(user.id)
            except Exception: pass


# ── Vercel HTTP Handler ───────────────────────────────────────────────────────

async def _process(body: bytes):
    app = await get_application()
    update = Update.de_json(json.loads(body), app.bot)
    await app.process_update(update)


class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body   = self.rfile.read(length)
        try:
            try:
                loop = asyncio.get_event_loop()
                if loop.is_closed():
                    raise RuntimeError
                loop.run_until_complete(_process(body))
            except RuntimeError:
                asyncio.run(_process(body))
        except Exception as e:
            print(f"Webhook error: {e}")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"WOXHUB Bot is running OK")

    def log_message(self, fmt, *args):
        pass
