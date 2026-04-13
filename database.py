# database.py — SQLite handler for WOXHUB Community Bot (Extended)
import os
import aiosqlite
import logging
from datetime import datetime

DB_PATH = os.getenv("DB_PATH", "/tmp/woxhub.db" if os.getenv("VERCEL") else "woxhub.db")
logger = logging.getLogger(__name__)

SCORE_ACTIONS = {
    "view_woxbot":      10,
    "click_broker":     15,
    "view_woxbiz":       8,
    "view_woxdemy":      8,
    "view_rewards":      5,
    "ask_price":        12,
    "verified":         20,
    "referral_made":    25,
    "faq_engaged":       3,
}


# ── Init ──────────────────────────────────────────────────────────────────────

async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS members (
                user_id     INTEGER PRIMARY KEY,
                username    TEXT,
                full_name   TEXT,
                join_date   TEXT,
                verified    INTEGER DEFAULT 0,
                referred_by INTEGER,
                score       INTEGER DEFAULT 0,
                warn_count  INTEGER DEFAULT 0
            )
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS referrals (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                referrer_id INTEGER NOT NULL,
                referee_id  INTEGER NOT NULL,
                created_at  TEXT NOT NULL,
                UNIQUE(referrer_id, referee_id)
            )
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS score_log (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id     INTEGER NOT NULL,
                action      TEXT NOT NULL,
                points      INTEGER NOT NULL,
                created_at  TEXT NOT NULL
            )
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS warnings (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id     INTEGER NOT NULL,
                reason      TEXT,
                warned_at   TEXT NOT NULL
            )
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS signals (
                id              INTEGER PRIMARY KEY AUTOINCREMENT,
                message_id      INTEGER,
                channel_id      INTEGER,
                content_preview TEXT,
                forwarded_at    TEXT
            )
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS faq_log (
                id              INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id         INTEGER,
                matched_keyword TEXT,
                question_text   TEXT,
                replied_at      TEXT
            )
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS polls (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                poll_id     TEXT UNIQUE,
                question    TEXT,
                created_at  TEXT,
                closed_at   TEXT,
                result_json TEXT
            )
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS seeded_posts (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                job_name    TEXT,
                message_id  INTEGER,
                seeded_at   TEXT
            )
        """)
        await db.commit()
    logger.info("Database initialised.")


# ── Members ───────────────────────────────────────────────────────────────────

async def upsert_member(user_id: int, username: str, full_name: str,
                        referred_by: int | None = None):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            INSERT INTO members (user_id, username, full_name, join_date, referred_by)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(user_id) DO UPDATE SET
                username  = excluded.username,
                full_name = excluded.full_name
        """, (user_id, username, full_name,
              datetime.utcnow().isoformat(), referred_by))
        await db.commit()


async def get_member(user_id: int) -> dict | None:
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute(
            "SELECT * FROM members WHERE user_id = ?", (user_id,)
        ) as cur:
            row = await cur.fetchone()
            return dict(row) if row else None


async def set_verified(user_id: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "UPDATE members SET verified = 1 WHERE user_id = ?", (user_id,)
        )
        await db.commit()


async def is_verified(user_id: int) -> bool:
    m = await get_member(user_id)
    return bool(m and m["verified"])


async def get_all_member_ids() -> list[int]:
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT user_id FROM members") as cur:
            rows = await cur.fetchall()
            return [r[0] for r in rows]


# ── Referrals ─────────────────────────────────────────────────────────────────

async def add_referral(referrer_id: int, referee_id: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            INSERT OR IGNORE INTO referrals (referrer_id, referee_id, created_at)
            VALUES (?, ?, ?)
        """, (referrer_id, referee_id, datetime.utcnow().isoformat()))
        await db.commit()


async def count_referrals(user_id: int) -> int:
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute(
            "SELECT COUNT(*) FROM referrals WHERE referrer_id = ?", (user_id,)
        ) as cur:
            row = await cur.fetchone()
            return row[0] if row else 0


# ── Lead Scoring ──────────────────────────────────────────────────────────────

async def add_score(user_id: int, action: str):
    points = SCORE_ACTIONS.get(action, 3)
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "UPDATE members SET score = score + ? WHERE user_id = ?",
            (points, user_id)
        )
        await db.execute("""
            INSERT INTO score_log (user_id, action, points, created_at)
            VALUES (?, ?, ?, ?)
        """, (user_id, action, points, datetime.utcnow().isoformat()))
        await db.commit()


async def get_score(user_id: int) -> int:
    m = await get_member(user_id)
    return m["score"] if m else 0


# ── Warnings ──────────────────────────────────────────────────────────────────

async def add_warning(user_id: int, reason: str) -> int:
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            INSERT INTO warnings (user_id, reason, warned_at)
            VALUES (?, ?, ?)
        """, (user_id, reason, datetime.utcnow().isoformat()))
        await db.execute(
            "UPDATE members SET warn_count = warn_count + 1 WHERE user_id = ?",
            (user_id,)
        )
        await db.commit()
        async with db.execute(
            "SELECT warn_count FROM members WHERE user_id = ?", (user_id,)
        ) as cur:
            row = await cur.fetchone()
            return row[0] if row else 1


async def get_warn_count(user_id: int) -> int:
    m = await get_member(user_id)
    return m["warn_count"] if m else 0


async def reset_warnings(user_id: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "UPDATE members SET warn_count = 0 WHERE user_id = ?", (user_id,)
        )
        await db.commit()


async def get_warned_members() -> list[dict]:
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute("""
            SELECT m.user_id, m.username, m.full_name, m.warn_count
            FROM members m WHERE m.warn_count > 0
            ORDER BY m.warn_count DESC
        """) as cur:
            rows = await cur.fetchall()
            return [dict(r) for r in rows]


# ── Stats ─────────────────────────────────────────────────────────────────────

async def get_total_members() -> int:
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT COUNT(*) FROM members") as cur:
            row = await cur.fetchone()
            return row[0] if row else 0


async def get_top_referrers(limit: int = 5) -> list[dict]:
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute("""
            SELECT m.username, m.full_name, COUNT(r.id) AS total
            FROM referrals r
            JOIN members m ON m.user_id = r.referrer_id
            GROUP BY r.referrer_id
            ORDER BY total DESC
            LIMIT ?
        """, (limit,)) as cur:
            rows = await cur.fetchall()
            return [dict(r) for r in rows]


async def get_high_score_members(min_score: int = 50) -> list[dict]:
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute("""
            SELECT user_id, username, full_name, score, warn_count
            FROM members WHERE score >= ?
            ORDER BY score DESC
        """, (min_score,)) as cur:
            rows = await cur.fetchall()
            return [dict(r) for r in rows]


# ── Signals ───────────────────────────────────────────────────────────────────

async def log_signal(message_id: int, channel_id: int, preview: str):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            INSERT INTO signals (message_id, channel_id, content_preview, forwarded_at)
            VALUES (?, ?, ?, ?)
        """, (message_id, channel_id, preview[:200], datetime.utcnow().isoformat()))
        await db.commit()


async def get_signal_count(days: int = 7) -> int:
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("""
            SELECT COUNT(*) FROM signals
            WHERE forwarded_at >= datetime('now', ?)
        """, (f"-{days} days",)) as cur:
            row = await cur.fetchone()
            return row[0] if row else 0


# ── FAQ Log ───────────────────────────────────────────────────────────────────

async def log_faq_reply(user_id: int, keyword: str, question_text: str):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            INSERT INTO faq_log (user_id, matched_keyword, question_text, replied_at)
            VALUES (?, ?, ?, ?)
        """, (user_id, keyword, question_text[:300], datetime.utcnow().isoformat()))
        await db.commit()


async def get_faq_stats(limit: int = 10) -> list[dict]:
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute("""
            SELECT matched_keyword, COUNT(*) as hits
            FROM faq_log
            GROUP BY matched_keyword
            ORDER BY hits DESC
            LIMIT ?
        """, (limit,)) as cur:
            rows = await cur.fetchall()
            return [dict(r) for r in rows]


# ── Polls ─────────────────────────────────────────────────────────────────────

async def save_poll(poll_id: str, question: str):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            INSERT OR IGNORE INTO polls (poll_id, question, created_at)
            VALUES (?, ?, ?)
        """, (poll_id, question, datetime.utcnow().isoformat()))
        await db.commit()


async def get_open_poll() -> dict | None:
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute("""
            SELECT * FROM polls WHERE closed_at IS NULL
            ORDER BY created_at DESC LIMIT 1
        """) as cur:
            row = await cur.fetchone()
            return dict(row) if row else None


async def close_poll(poll_id: str, result_json: str):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            UPDATE polls SET closed_at = ?, result_json = ?
            WHERE poll_id = ?
        """, (datetime.utcnow().isoformat(), result_json, poll_id))
        await db.commit()


# ── Seeded Posts ──────────────────────────────────────────────────────────────

async def log_seeded_post(job_name: str, message_id: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            INSERT INTO seeded_posts (job_name, message_id, seeded_at)
            VALUES (?, ?, ?)
        """, (job_name, message_id, datetime.utcnow().isoformat()))
        await db.commit()


async def get_last_seeded_index(job_name: str) -> int:
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("""
            SELECT COUNT(*) FROM seeded_posts WHERE job_name = ?
        """, (job_name,)) as cur:
            row = await cur.fetchone()
            return row[0] if row else 0
