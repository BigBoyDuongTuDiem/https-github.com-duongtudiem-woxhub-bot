# config.py — WOXHUB Bot Configuration
# ═══════════════════════════════════════════════════════════
#  ĐIỀN THÔNG TIN CỦA BẠN VÀO ĐÂY (hoặc dùng file .env)
# ═══════════════════════════════════════════════════════════
import os
from dotenv import load_dotenv

load_dotenv()

# ── Bot Credentials ───────────────────────────────────────
BOT_TOKEN            = os.getenv("BOT_TOKEN", "8591730050:AAFpUzYMeATZYD44jkPBvRTK7atYazU_PdE")
GROUP_ID             = int(os.getenv("GROUP_ID", "0"))           # Số âm, vd: -1001234567890
SIGNAL_CHANNEL_ID    = int(os.getenv("SIGNAL_CHANNEL_ID", "0"))  # Channel WOXBOT SIGNAL

# ── Admin ─────────────────────────────────────────────────
ADMIN_USER_ID        = int(os.getenv("ADMIN_USER_ID", "8526654653"))
ADMIN_USERNAME       = os.getenv("ADMIN_USERNAME", "BIGBOY_WOXBAL")
ADMIN_IDS            = [ADMIN_USER_ID]  # Thêm ID admin phụ nếu cần

# ── Broker Referral Links ─────────────────────────────────
BROKER_LINK_PUPRIME   = os.getenv("BROKER_LINK_PUPRIME", "https://puvip.co/la-partners/vn/oQNwN5Yi")
BROKER_LINK_TOMO      = os.getenv("BROKER_LINK_TOMO", "https://client.tomologin.com/register/trader?link_id=cita3dyi&referrer_id=a0901495")
BROKER_LINK_DBG       = os.getenv("BROKER_LINK_DBG", "https://dbgvn.com/account/register?shareUserSetId=52af1f15979540ee8")

# ── Bot Username (for referral deep links) ────────────────
BOT_USERNAME         = os.getenv("BOT_USERNAME", "woxhub_community_bot")

# ── Moderation ────────────────────────────────────────────
MAX_WARNINGS         = 3
RATE_LIMIT_MESSAGES  = 5    # Số tin nhắn tối đa trong khoảng thời gian
RATE_LIMIT_WINDOW    = 10   # Giây

# ── Database ──────────────────────────────────────────────
DB_PATH              = os.getenv("DB_PATH", "woxhub.db")

# ── Scheduler Timezone ────────────────────────────────────
TIMEZONE             = "Asia/Ho_Chi_Minh"

# ── Signal Forwarding ─────────────────────────────────────
SIGNAL_ENABLED       = True   # Toggle bật/tắt tín hiệu
