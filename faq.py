# faq.py — FAQ Auto-Reply Engine for WOXHUB Community Bot
import json
import logging
import unicodedata
import re
from pathlib import Path
from telegram.constants import ParseMode
import database as db
import messages as msg
import keyboards as kb

logger = logging.getLogger(__name__)

_FAQ_FILE = Path(__file__).parent / "data" / "faq_rules.json"
_faq_rules: list[dict] = []

# Cooldown: (user_id, response_key) → timestamp
_faq_cooldown: dict[tuple, float] = {}
FAQ_COOLDOWN_SECONDS = 3600  # 1 giờ


def load_faq_rules() -> list[dict]:
    """Load và parse faq_rules.json. Có thể gọi lại để hot-reload."""
    global _faq_rules
    try:
        with open(_FAQ_FILE, encoding="utf-8") as f:
            data = json.load(f)
        _faq_rules = data.get("rules", [])
        # Sort by priority descending
        _faq_rules.sort(key=lambda r: r.get("priority", 0), reverse=True)
        logger.info("FAQ rules loaded: %d rules", len(_faq_rules))
        return _faq_rules
    except Exception as e:
        logger.error("Failed to load FAQ rules: %s", e)
        return []


def _normalize(text: str) -> str:
    """Chuẩn hóa: bỏ dấu tiếng Việt, lowercase, bỏ dấu câu."""
    # Decompose unicode (NFD) then drop combining marks = remove diacritics
    nfkd = unicodedata.normalize("NFKD", text)
    ascii_text = "".join(c for c in nfkd if not unicodedata.combining(c))
    # Lowercase + remove punctuation
    ascii_text = ascii_text.lower()
    ascii_text = re.sub(r"[^\w\s]", " ", ascii_text)
    return ascii_text


def detect_faq(message_text: str) -> str | None:
    """
    Kiểm tra tin nhắn có khớp FAQ không.
    Trả về response_key nếu khớp, None nếu không.
    """
    if not _faq_rules:
        load_faq_rules()

    normalized = _normalize(message_text)

    for rule in _faq_rules:
        for keyword in rule.get("keywords", []):
            norm_kw = _normalize(keyword)
            if norm_kw in normalized:
                return rule["response_key"]
    return None


def _is_on_cooldown(user_id: int, response_key: str) -> bool:
    """Kiểm tra user có đang trong thời gian cooldown cho FAQ này không."""
    import time
    key = (user_id, response_key)
    last = _faq_cooldown.get(key)
    if last is None:
        return False
    return (time.time() - last) < FAQ_COOLDOWN_SECONDS


def _set_cooldown(user_id: int, response_key: str):
    import time
    _faq_cooldown[(user_id, response_key)] = time.time()


async def faq_message_handler(update, context):
    """
    MessageHandler entry point.
    Kiểm tra mọi tin nhắn text trong nhóm xem có FAQ keyword không.
    """
    from config import GROUP_ID, ADMIN_IDS
    message = update.message
    if not message or not message.text:
        return
    if message.chat.id != GROUP_ID:
        return
    user = message.from_user
    if user.id in ADMIN_IDS:
        return

    response_key = detect_faq(message.text)
    if not response_key:
        return

    # Cooldown check — tránh spam auto-reply cùng một topic
    if _is_on_cooldown(user.id, response_key):
        return

    response_text = msg.FAQ_RESPONSES.get(response_key)
    if not response_text:
        return

    # Gửi reply + track
    await message.reply_text(
        response_text,
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=kb.faq_back_keyboard(),
    )

    _set_cooldown(user.id, response_key)
    await db.log_faq_reply(user.id, response_key, message.text)
    await db.add_score(user.id, "faq_engaged")


async def faq_quick_reply(query, context):
    """
    Callback handler cho nút bấm FAQ trong faq_menu_keyboard.
    data = "faq_<key>"
    """
    user = query.from_user
    key = query.data  # e.g. "faq_bot_safe"

    response_text = msg.FAQ_RESPONSES.get(key)
    if not response_text:
        await query.answer("Không tìm thấy câu trả lời.", show_alert=True)
        return

    await query.edit_message_text(
        response_text,
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=kb.faq_back_keyboard(),
    )
    await db.log_faq_reply(user.id, key, f"menu_click:{key}")
    await db.add_score(user.id, "faq_engaged")
