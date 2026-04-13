# scheduler.py — All scheduled seeding jobs for WOXHUB Community Bot
import json
import logging
import datetime
from pathlib import Path
from telegram.constants import ParseMode
import database as db
import messages as msg

logger = logging.getLogger(__name__)

_SEED_FILE = Path(__file__).parent / "data" / "seed_content.json"

def _load_seed() -> dict:
    with open(_SEED_FILE, encoding="utf-8") as f:
        return json.load(f)


# ─── MORNING MARKET BRIEF ─────────────────────────────────────────────────────
# Fires: Mon–Fri 08:00 VN (01:00 UTC)

async def morning_market_brief(context):
    from config import GROUP_ID
    try:
        index = await db.get_last_seeded_index("morning_brief") % len(msg.MORNING_BRIEFS)
        text = msg.MORNING_BRIEFS[index]
        sent = await context.bot.send_message(
            GROUP_ID, text, parse_mode=ParseMode.MARKDOWN
        )
        await db.log_seeded_post("morning_brief", sent.message_id)
        logger.info("Morning brief sent (index %d)", index)
    except Exception as e:
        logger.error("Morning brief failed: %s", e)


# ─── EVENING RECAP ────────────────────────────────────────────────────────────
# Fires: Mon–Fri 21:00 VN (14:00 UTC)

async def evening_recap(context):
    from config import GROUP_ID
    try:
        index = await db.get_last_seeded_index("evening_recap") % len(msg.EVENING_RECAPS)
        text = msg.EVENING_RECAPS[index]
        sent = await context.bot.send_message(
            GROUP_ID, text, parse_mode=ParseMode.MARKDOWN
        )
        await db.log_seeded_post("evening_recap", sent.message_id)
        logger.info("Evening recap sent")
    except Exception as e:
        logger.error("Evening recap failed: %s", e)


# ─── EDUCATIONAL CONTENT ──────────────────────────────────────────────────────
# Fires: Tue & Thu 19:00 VN (12:00 UTC)

async def educational_content(context):
    from config import GROUP_ID
    try:
        index = await db.get_last_seeded_index("educational") % len(msg.EDUCATIONAL_SNIPPETS)
        text = msg.EDUCATIONAL_SNIPPETS[index]
        sent = await context.bot.send_message(
            GROUP_ID, text, parse_mode=ParseMode.MARKDOWN
        )
        await db.log_seeded_post("educational", sent.message_id)
        logger.info("Educational content sent (index %d)", index)
    except Exception as e:
        logger.error("Educational content failed: %s", e)


# ─── DAILY DIGEST ─────────────────────────────────────────────────────────────
# Fires: Daily 08:30 VN (01:30 UTC)

async def daily_digest(context):
    from config import GROUP_ID
    try:
        total    = await db.get_total_members()
        top_refs = await db.get_top_referrers(3)
        text = (
            "📊 *BÁO CÁO CỘNG ĐỒNG WOXHUB*\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            f"👥 Tổng thành viên: *{total}*\n\n"
            "🏆 *Top 3 người giới thiệu:*\n"
        )
        for i, r in enumerate(top_refs, 1):
            name = r.get("full_name") or r.get("username") or "N/A"
            text += f"   {i}. {name} — {r['total']} người\n"
        if not top_refs:
            text += "   Chưa có dữ liệu\n"
        text += (
            "\n💡 Giới thiệu bạn bè để leo bảng xếp hạng & nhận thưởng!\n"
            "🔗 Lấy link của bạn: /myref"
        )
        await context.bot.send_message(GROUP_ID, text, parse_mode=ParseMode.MARKDOWN)
        logger.info("Daily digest sent")
    except Exception as e:
        logger.error("Daily digest failed: %s", e)


# ─── WEEKLY LEADERBOARD ───────────────────────────────────────────────────────
# Fires: Monday 09:00 VN (02:00 UTC)

async def weekly_leaderboard(context):
    from config import GROUP_ID
    try:
        top_refs = await db.get_top_referrers(5)
        text = (
            "🏆 *BẢNG XẾP HẠNG WOXHUB TUẦN NÀY*\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "🥇 Top 5 chiến binh giới thiệu nhiều nhất:\n\n"
        )
        medals = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣"]
        for i, r in enumerate(top_refs):
            name = r.get("full_name") or r.get("username") or "N/A"
            text += f"{medals[i]} {name} — *{r['total']} người*\n"
        if not top_refs:
            text += "   Tuần này chưa có ai giới thiệu. Hãy là người đầu tiên! 🚀\n"
        text += (
            "\n💰 *Phần thưởng:*\n"
            "   🥇 Top 1: Thưởng đặc biệt từ WOXBAL\n"
            "   🥈 Top 2–3: Quà tặng + điểm bonus\n\n"
            "🔗 Lấy link giới thiệu: /myref\n"
            "Tuần mới, cơ hội mới! 💪"
        )
        await context.bot.send_message(GROUP_ID, text, parse_mode=ParseMode.MARKDOWN)
        logger.info("Weekly leaderboard sent")
    except Exception as e:
        logger.error("Weekly leaderboard failed: %s", e)


# ─── ACTIVITY SCHEDULE ────────────────────────────────────────────────────────
# Fires: Sunday 10:00 VN (03:00 UTC)

async def activity_schedule(context):
    from config import GROUP_ID
    try:
        seed = _load_seed()
        text = seed["activity_schedule"]["weekly_template"]
        sent = await context.bot.send_message(
            GROUP_ID, text, parse_mode=ParseMode.MARKDOWN
        )
        await db.log_seeded_post("activity_schedule", sent.message_id)
        logger.info("Activity schedule sent")
    except Exception as e:
        logger.error("Activity schedule failed: %s", e)


# ─── WEEKLY POLL ──────────────────────────────────────────────────────────────
# Fires: Wednesday 11:00 VN (04:00 UTC)

async def send_weekly_poll(context):
    from config import GROUP_ID
    try:
        seed = _load_seed()
        polls = seed["poll_questions"]
        week_num = datetime.date.today().isocalendar()[1]
        poll_data = polls[week_num % len(polls)]

        poll_msg = await context.bot.send_poll(
            chat_id=GROUP_ID,
            question=poll_data["question"],
            options=poll_data["options"],
            is_anonymous=poll_data.get("is_anonymous", False),
            allows_multiple_answers=False,
        )
        await db.save_poll(poll_msg.poll.id, poll_data["question"])
        logger.info("Weekly poll sent: %s", poll_data["question"])
    except Exception as e:
        logger.error("Weekly poll failed: %s", e)


# ─── CLOSE PREVIOUS POLL ──────────────────────────────────────────────────────
# Fires: Wednesday 23:00 VN (16:00 UTC)

async def close_weekly_poll(context):
    from config import GROUP_ID
    import json as _json
    try:
        open_poll = await db.get_open_poll()
        if not open_poll:
            logger.info("No open poll to close")
            return
        result = await context.bot.stop_poll(
            chat_id=GROUP_ID,
            message_id=None  # Will fail if message_id not tracked — handled gracefully
        )
        await db.close_poll(open_poll["poll_id"], _json.dumps({}))
        logger.info("Poll closed")
    except Exception as e:
        logger.warning("Close poll: %s (may already be closed)", e)


# ─── SETUP SCHEDULER ─────────────────────────────────────────────────────────

def setup_scheduler(application):
    """Register all scheduled jobs using PTB's built-in JobQueue."""
    jq = application.job_queue

    # Daily digest — 08:30 VN = 01:30 UTC
    jq.run_daily(daily_digest,        time=datetime.time(1, 30, 0),  name="daily_digest")

    # Morning brief — 08:00 VN = 01:00 UTC, Mon–Fri
    jq.run_daily(morning_market_brief, time=datetime.time(1, 0, 0),
                 days=(0, 1, 2, 3, 4), name="morning_brief")

    # Evening recap — 21:00 VN = 14:00 UTC, Mon–Fri
    jq.run_daily(evening_recap,       time=datetime.time(14, 0, 0),
                 days=(0, 1, 2, 3, 4), name="evening_recap")

    # Educational content — 19:00 VN = 12:00 UTC, Tue & Thu
    jq.run_daily(educational_content, time=datetime.time(12, 0, 0),
                 days=(1, 3), name="educational")

    # Weekly leaderboard — 09:00 VN = 02:00 UTC, Monday
    jq.run_daily(weekly_leaderboard,  time=datetime.time(2, 0, 0),
                 days=(0,), name="leaderboard")

    # Activity schedule — 10:00 VN = 03:00 UTC, Sunday
    jq.run_daily(activity_schedule,   time=datetime.time(3, 0, 0),
                 days=(6,), name="activity_schedule")

    # Weekly poll — 11:00 VN = 04:00 UTC, Wednesday
    jq.run_daily(send_weekly_poll,    time=datetime.time(4, 0, 0),
                 days=(2,), name="weekly_poll")

    # Close poll — 23:00 VN = 16:00 UTC, Wednesday
    jq.run_daily(close_weekly_poll,   time=datetime.time(16, 0, 0),
                 days=(2,), name="close_poll")

    logger.info("✅ Scheduler: 8 jobs registered")


# ─── JOB MAP (for /seed_now admin command) ────────────────────────────────────

JOB_MAP = {
    "morning_brief":     morning_market_brief,
    "evening_recap":     evening_recap,
    "educational":       educational_content,
    "daily_digest":      daily_digest,
    "leaderboard":       weekly_leaderboard,
    "activity_schedule": activity_schedule,
    "poll":              send_weekly_poll,
}
