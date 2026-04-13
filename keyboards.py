# keyboards.py — All inline keyboard layouts for WOXHUB Community Bot
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


# ── Main Menu ─────────────────────────────────────────────────────────────────

def main_menu_keyboard() -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton("📜 Nội Quy Nhóm", callback_data="noi_quy"),
            InlineKeyboardButton("🌐 Dự Án WOXBAL", callback_data="woxbal_projects"),
        ],
        [
            InlineKeyboardButton("🏦 Đăng Ký Sàn", callback_data="dang_ky_san"),
            InlineKeyboardButton("🎁 Quyền Lợi & Thưởng", callback_data="quyen_loi"),
        ],
        [
            InlineKeyboardButton("❓ Câu Hỏi Thường Gặp", callback_data="faq_menu"),
            InlineKeyboardButton("🎧 Hỗ Trợ Admin", callback_data="support"),
        ],
    ]
    return InlineKeyboardMarkup(buttons)


# ── Welcome Keyboard (Bot247 style) ───────────────────────────────────────────

def welcome_keyboard() -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(
                "✅ Đọc & Đồng Ý Nội Quy Nhóm",
                callback_data="verify_member"
            )
        ],
        [
            InlineKeyboardButton("📜 Nội Quy", callback_data="noi_quy"),
            InlineKeyboardButton("🎁 Quyền Lợi", callback_data="quyen_loi"),
        ],
        [
            InlineKeyboardButton("🏦 Đăng Ký Sàn", callback_data="dang_ky_san"),
            InlineKeyboardButton("🌐 Dự Án WOXBAL", callback_data="woxbal_projects"),
        ],
        [
            InlineKeyboardButton("🎧 Hỗ Trợ", callback_data="support"),
        ],
    ]
    return InlineKeyboardMarkup(buttons)


# ── Nội Quy ───────────────────────────────────────────────────────────────────

def noi_quy_keyboard(verified: bool = False) -> InlineKeyboardMarkup:
    buttons = []
    if not verified:
        buttons.append([
            InlineKeyboardButton(
                "✅ Tôi Đã Đọc & Đồng Ý Nội Quy",
                callback_data="verify_member"
            )
        ])
    buttons.append([InlineKeyboardButton("🔙 Quay lại Menu", callback_data="main_menu")])
    return InlineKeyboardMarkup(buttons)


def verify_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "✅ Tôi Đã Đọc & Đồng Ý Nội Quy",
                callback_data="verify_member"
            )
        ]
    ])


# ── Quyền Lợi & Phần Thưởng ──────────────────────────────────────────────────

def quyen_loi_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🏦 Đăng Ký Nhận Quyền Lợi", callback_data="dang_ky_san")],
        [InlineKeyboardButton("🔗 Link Giới Thiệu Của Tôi", callback_data="my_ref")],
        [InlineKeyboardButton("🔙 Quay lại Menu", callback_data="main_menu")],
    ])


# ── Đăng Ký Sàn ───────────────────────────────────────────────────────────────

def dang_ky_san_keyboard(puprime_link: str, tomo_link: str, dbg_link: str, admin_username: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔴 Đăng Ký PU Prime", url=puprime_link)],
        [InlineKeyboardButton("🟡 Đăng Ký Tomo Trader", url=tomo_link)],
        [InlineKeyboardButton("🔵 Đăng Ký DBG", url=dbg_link)],
        [InlineKeyboardButton(f"📩 Báo ID cho Admin @{admin_username}", url=f"https://t.me/{admin_username}")],
        [InlineKeyboardButton("🔙 Quay lại Menu", callback_data="main_menu")],
    ])


# ── Dự Án WOXBAL ──────────────────────────────────────────────────────────────

def woxbal_projects_keyboard() -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton("🤖 WOXBOT", callback_data="project_woxbot"),
            InlineKeyboardButton("💎 WOXBIZ", callback_data="project_woxbiz"),
        ],
        [
            InlineKeyboardButton("🎓 WOXDEMY", callback_data="project_woxdemy"),
        ],
        [
            InlineKeyboardButton("🔙 Quay lại Menu", callback_data="main_menu"),
        ],
    ]
    return InlineKeyboardMarkup(buttons)


def back_to_projects_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 Quay lại Dự Án", callback_data="woxbal_projects")],
        [InlineKeyboardButton("🏠 Menu chính", callback_data="main_menu")],
    ])


# ── FAQ Menu ──────────────────────────────────────────────────────────────────

def faq_menu_keyboard() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton("🤖 WOXBOT có an toàn không?", callback_data="faq_bot_safe")],
        [InlineKeyboardButton("💰 Vốn bao nhiêu để bắt đầu?", callback_data="faq_capital")],
        [InlineKeyboardButton("🤝 IB hoạt động như thế nào?", callback_data="faq_ib")],
        [InlineKeyboardButton("📊 Winrate tín hiệu là bao nhiêu?", callback_data="faq_winrate")],
        [InlineKeyboardButton("💸 Rút tiền như thế nào?", callback_data="faq_withdraw")],
        [InlineKeyboardButton("💎 WOXBIZ giá bao nhiêu?", callback_data="faq_woxbiz")],
        [InlineKeyboardButton("⚙️ Cài đặt WOXBOT như thế nào?", callback_data="faq_setup_bot")],
        [InlineKeyboardButton("🔙 Quay lại Menu", callback_data="main_menu")],
    ]
    return InlineKeyboardMarkup(buttons)


def faq_back_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("❓ Câu hỏi khác", callback_data="faq_menu")],
        [InlineKeyboardButton("🎧 Hỏi Admin trực tiếp", callback_data="support")],
        [InlineKeyboardButton("🔙 Menu chính", callback_data="main_menu")],
    ])


# ── Support ───────────────────────────────────────────────────────────────────

def support_keyboard(admin_username: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(f"💬 Nhắn @{admin_username} ngay", url=f"https://t.me/{admin_username}")],
        [InlineKeyboardButton("❓ Xem FAQ", callback_data="faq_menu")],
        [InlineKeyboardButton("🔙 Quay lại Menu", callback_data="main_menu")],
    ])


# ── Signal ────────────────────────────────────────────────────────────────────

def signal_keyboard(puprime_link: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔴 Đăng Ký PU Prime Nhận Tín Hiệu", url=puprime_link)],
    ])


# ── Back ──────────────────────────────────────────────────────────────────────

def back_to_main_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 Quay lại Menu chính", callback_data="main_menu")]
    ])
