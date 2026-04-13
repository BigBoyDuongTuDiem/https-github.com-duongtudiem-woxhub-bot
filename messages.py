# messages.py — All Vietnamese message templates for WOXHUB Community Bot

# ═══════════════════════════════════════════════════════
#  WELCOME & START
# ═══════════════════════════════════════════════════════

def welcome_new_member(full_name: str) -> str:
    return (
        f"🎉 *Chào mừng {full_name} đến với WOXHUB!* 🎉\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n"
        "🌟 Bạn vừa gia nhập cộng đồng trader Forex/Vàng\n"
        "hàng đầu Việt Nam được dẫn dắt bởi *WOXBAL TEAM*!\n\n"
        "📋 *Để được tham gia đầy đủ, vui lòng:*\n"
        "1️⃣ Nhấn *✅ Đọc & Đồng ý Nội Quy* bên dưới\n"
        "2️⃣ Đăng ký tài khoản sàn qua link của nhóm\n"
        "3️⃣ Báo admin ID tài khoản để kích hoạt quyền lợi\n\n"
        "⚠️ *Chưa xác nhận sẽ bị hạn chế gửi tin nhắn.*\n\n"
        "👇 Khám phá quyền lợi & dự án WOXBAL bên dưới:"
    )


def start_message(full_name: str) -> str:
    return (
        f"👋 *Xin chào {full_name}!*\n\n"
        "🏆 Chào mừng đến với *WOXHUB* — Cộng đồng trader\n"
        "thông minh được vận hành bởi *WOXBAL TEAM*!\n\n"
        "💡 *Hệ sinh thái WOXBAL gồm:*\n"
        "   🤖 *WOXBOT* — Robot giao dịch tự động XAU/USD\n"
        "   💎 *WOXBIZ* — Cộng đồng VIP & thu nhập IB\n"
        "   🎓 *WOXDEMY* — Đào tạo Trader A-Z\n\n"
        "👇 *Chọn mục bạn muốn khám phá:*"
    )


# ═══════════════════════════════════════════════════════
#  NỘI QUY NHÓM
# ═══════════════════════════════════════════════════════

NOI_QUY = (
    "📜 *NỘI QUY NHÓM WOXHUB*\n"
    "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
    "⛔ *CÁC HÀNH VI BỊ CẤM:*\n"
    "❌ Spam, quảng cáo dịch vụ ngoài nhóm\n"
    "❌ Chia sẻ link lạ chưa được admin duyệt\n"
    "❌ Xúc phạm, chửi thề, nội dung 18+\n"
    "❌ Bơm thổi, thông tin sai lệch về thị trường\n"
    "❌ Lừa đảo, kêu gọi đầu tư cá nhân\n"
    "❌ Chia sẻ tín hiệu từ nguồn khác trong nhóm\n\n"
    "⚠️ *HÌNH THỨC XỬ PHẠT:*\n"
    "   • Vi phạm lần 1: Cảnh cáo\n"
    "   • Vi phạm lần 2: Cảnh cáo + mute 24h\n"
    "   • Vi phạm lần 3: Kick vĩnh viễn\n\n"
    "✅ *ĐỂ NHẬN QUYỀN LỢI NHÓM:*\n"
    "   📌 Đăng ký tài khoản sàn qua link của nhóm\n"
    "   📌 Báo admin ID để kích hoạt\n"
    "   📌 Tham gia hoạt động nhóm mỗi tuần\n\n"
    "💬 Mọi thắc mắc liên hệ admin để được hỗ trợ."
)

VERIFICATION_SUCCESS = (
    "✅ *Xác nhận thành công!*\n\n"
    "🎊 Chào mừng bạn chính thức gia nhập *WOXHUB Community*!\n\n"
    "🚀 Bạn đã được mở khóa quyền gửi tin nhắn trong nhóm.\n\n"
    "📌 *Bước tiếp theo để nhận đầy đủ quyền lợi:*\n"
    "   1️⃣ Đăng ký tài khoản sàn qua link nhóm\n"
    "   2️⃣ Báo ID tài khoản cho admin\n"
    "   3️⃣ Nhận tín hiệu & hoa hồng IB\n\n"
    "Gõ /menu để xem tất cả tính năng!"
)


# ═══════════════════════════════════════════════════════
#  QUYỀN LỢI & PHẦN THƯỞNG
# ═══════════════════════════════════════════════════════

QUYEN_LOI = (
    "🎁 *QUYỀN LỢI THÀNH VIÊN WOXHUB*\n"
    "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
    "🔹 Nhận tín hiệu XAU/USD & Forex *hàng ngày* từ WOXBOT\n"
    "🔹 Truy cập kho tài liệu phân tích thị trường miễn phí\n"
    "🔹 Hỗ trợ kỹ thuật & tư vấn chiến lược 1-1\n"
    "🔹 Ưu tiên tham gia event & webinar của WOXBAL\n"
    "🔹 Thu nhập thụ động qua chương trình IB\n\n"
    "💰 *HỆ THỐNG PHẦN THƯỞNG:*\n\n"
    "👤 *Cá nhân:*\n"
    "   🔸 Hoàn phí spread: $2–$5/lot\n"
    "   🔸 Giới thiệu 1 người đăng ký sàn: $10–$30\n"
    "   🔸 Thành viên VIP WOXBIZ: +$5/lot từ downline\n\n"
    "👥 *Đội nhóm (Team IB):*\n"
    "   🥉 Bronze ≥5 người: +10% hoa hồng\n"
    "   🥈 Silver ≥15 người: +20% + badge đặc biệt\n"
    "   🥇 Gold ≥30 người: +35% + ưu tiên event\n"
    "   💎 Diamond ≥50 người: Revenue share + hỗ trợ riêng\n\n"
    "📊 *ĐIỂM TÍCH LŨY:*\n"
    "   • Xem WOXBOT: +10đ | Đăng ký sàn: +15đ\n"
    "   • Giới thiệu thành viên: +25đ\n"
    "   • Tích 100đ = quà tặng từ WOXBAL 🎁\n\n"
    "🔗 Xem link giới thiệu: /myref\n"
    "📈 Xem điểm của bạn: /score"
)


# ═══════════════════════════════════════════════════════
#  ĐĂNG KÝ SÀN
# ═══════════════════════════════════════════════════════

def dang_ky_san_message(broker_puprime: str, broker_tomo: str, broker_dbg: str) -> str:
    return (
        "🏦 *ĐĂNG KÝ TÀI KHOẢN SÀN GIAO DỊCH*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "⚠️ *BẮT BUỘC đăng ký qua link của nhóm* để:\n"
        "✅ Được tính hoa hồng IB cho người giới thiệu\n"
        "✅ Nhận hoàn phí spread cao nhất\n"
        "✅ Được hỗ trợ nạp/rút bởi team WOXBAL 24/7\n"
        "✅ Kích hoạt tự động quyền lợi WOXHUB\n\n"
        f"🔴 *PU Prime* — Leverage cao, nạp rút nhanh VN\n"
        f"   Mã: `oQNwN5Yi`\n"
        f"   👉 {broker_puprime}\n\n"
        f"🟡 *Tomo Trader* — Sàn Việt, hỗ trợ 24/7 tiếng Việt\n"
        f"   👉 {broker_tomo}\n\n"
        f"🔵 *DBG* — Spread thấp, uy tín cao\n"
        f"   👉 {broker_dbg}\n\n"
        "📌 *Sau khi đăng ký:*\n"
        "   Nhắn admin ID tài khoản để kích hoạt quyền lợi!\n\n"
        "❓ Cần hỗ trợ? Nhấn *Liên hệ Admin* bên dưới."
    )


# ═══════════════════════════════════════════════════════
#  DỰ ÁN WOXBAL
# ═══════════════════════════════════════════════════════

WOXBAL_PROJECT_INTRO = (
    "🌐 *DỰ ÁN WOXBAL — HỆ SINH THÁI TÀI CHÍNH THÔNG MINH*\n"
    "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
    "💡 WOXBAL là hệ sinh thái tài chính tích hợp AI,\n"
    "giúp mọi người tiếp cận thị trường an toàn & hiệu quả.\n\n"
    "🏗️ *3 TRỤ CỘT WOXBAL:*\n\n"
    "🤖 *WOXBOT* — Robot giao dịch XAU/USD tự động\n"
    "💎 *WOXBIZ* — Cộng đồng VIP & hệ thống thu nhập IB\n"
    "🎓 *WOXDEMY* — Trung tâm đào tạo Trader A-Z\n\n"
    "👇 *Chọn để tìm hiểu chi tiết:*"
)

WOXBOT_INFO = (
    "🤖 *WOXBOT — ROBOT GIAO DỊCH TỰ ĐỘNG*\n"
    "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
    "⚡ WOXBOT là EA giao dịch XAU/USD & Forex được phát triển\n"
    "bởi đội ngũ quant trader WOXBAL sau 8 năm thực chiến.\n\n"
    "📦 *3 PHIÊN BẢN WOXBOT:*\n\n"
    "🟢 *AUTO (Tự động 100%)*\n"
    "   • Bot tự mở/đóng lệnh hoàn toàn\n"
    "   • Phù hợp người không có thời gian theo dõi\n"
    "   • Mục tiêu: 1–3%/ngày, drawdown <15%\n\n"
    "🟡 *½ AUTO (Bán tự động)*\n"
    "   • Bot phân tích, trader quyết định vào lệnh\n"
    "   • Kết hợp AI + kinh nghiệm thực tế\n\n"
    "🔵 *SIGNAL (Tín hiệu giao dịch)*\n"
    "   • Nhận tín hiệu real-time qua Telegram\n"
    "   • Entry, SL, TP rõ ràng — Winrate 72–80%\n\n"
    "📊 *KẾT QUẢ XÁC MINH:*\n"
    "   ✅ Tỷ lệ thành công: 80–90%\n"
    "   ✅ Cộng đồng 10.000+ thành viên đang dùng\n"
    "   ✅ Track record công khai, minh bạch 100%\n\n"
    "💬 Liên hệ admin để được tư vấn phiên bản phù hợp!"
)

WOXBIZ_INFO = (
    "💎 *WOXBIZ — CỘNG ĐỒNG VIP TRADER & THU NHẬP IB*\n"
    "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
    "🏆 WOXBIZ là cộng đồng VIP dành cho trader nghiêm túc\n"
    "muốn xây dựng thu nhập bền vững từ thị trường tài chính.\n\n"
    "💰 *GÓI THÀNH VIÊN:*\n"
    "   📌 *$150 / 6 tháng*\n"
    "   📌 *$250 / năm* (tiết kiệm 17%)\n\n"
    "✅ *QUYỀN LỢI WOXBIZ:*\n"
    "🔹 Nhận $5/lot từ volume trading của downline\n"
    "🔹 Group signal VIP riêng biệt — độ chính xác cao hơn\n"
    "🔹 Coaching 1-1 hàng tuần với mentor WOXBAL\n"
    "🔹 Tài liệu chiến lược & bộ tool độc quyền\n"
    "🔹 Hệ thống Funnel Automation sẵn dùng\n"
    "🔹 Hoa hồng $40/người giới thiệu trực tiếp\n"
    "🔹 100.000+ khách hàng tiềm năng sẵn có\n\n"
    "📈 *Thành viên active trung bình: $500–$2.000/tháng*\n\n"
    "💬 Đăng ký ngay — liên hệ admin để biết thêm!"
)

WOXDEMY_INFO = (
    "🎓 *WOXDEMY — TRUNG TÂM ĐÀO TẠO TRADER A-Z*\n"
    "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
    "📚 Lộ trình đào tạo hoàn chỉnh: người mới → chuyên nghiệp.\n\n"
    "🗂️ *CÁC KHÓA HỌC:*\n\n"
    "📗 *Cơ bản (MIỄN PHÍ cho thành viên WOXHUB):*\n"
    "   • Nền tảng Forex & XAU/USD từ đầu\n"
    "   • Đọc biểu đồ nến, quản lý vốn & tâm lý\n\n"
    "📘 *Nâng cao ($49):*\n"
    "   • Price Action chuyên sâu\n"
    "   • Chiến lược giao dịch theo xu hướng\n\n"
    "📕 *Chuyên gia ($149):*\n"
    "   • Xây dựng hệ thống giao dịch cá nhân\n"
    "   • Tối ưu EA với AI/Python\n"
    "   • Xây dựng thu nhập thụ động từ IB\n\n"
    "🏅 *Chứng chỉ hoàn thành được WOXBAL công nhận*\n\n"
    "💬 Đăng ký ngay — liên hệ admin!"
)


# ═══════════════════════════════════════════════════════
#  HỖ TRỢ
# ═══════════════════════════════════════════════════════

def support_message(admin_username: str) -> str:
    return (
        "🎧 *HỖ TRỢ WOXHUB*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"👤 *Admin chính:* @{admin_username}\n\n"
        "⏰ *Giờ hỗ trợ:* 8:00 – 22:00 (GMT+7)\n\n"
        "📌 *Các vấn đề thường gặp:*\n"
        "🔹 Đăng ký & xác minh tài khoản sàn\n"
        "🔹 Cài đặt & sử dụng WOXBOT EA\n"
        "🔹 Tư vấn gói WOXBIZ VIP\n"
        "🔹 Đăng ký khóa học WOXDEMY\n"
        "🔹 Câu hỏi về hoa hồng IB & rút tiền\n"
        "🔹 Báo lỗi kỹ thuật\n\n"
        "💬 Nhắn tin trực tiếp cho admin để được hỗ trợ nhanh nhất!\n\n"
        "⚡ Hoặc dùng /faq để xem câu trả lời thường gặp."
    )


# ═══════════════════════════════════════════════════════
#  REFERRAL & SCORE
# ═══════════════════════════════════════════════════════

def my_referral_message(username: str, ref_count: int, score: int, bot_username: str) -> str:
    ref_link = f"https://t.me/{bot_username}?start=REF_{username}" if username else "N/A"
    return (
        "🔗 *LINK GIỚI THIỆU CỦA BẠN*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"👤 Username: @{username}\n"
        f"🔗 Link ref:\n`{ref_link}`\n\n"
        f"📊 *Thống kê:*\n"
        f"   👥 Đã giới thiệu: *{ref_count} người*\n"
        f"   ⭐ Điểm tích lũy: *{score} điểm*\n\n"
        "💡 *Cách dùng:* Chia sẻ link này cho bạn bè.\n"
        "Khi họ /start bot qua link, bạn tự động nhận điểm thưởng!\n\n"
        "🎁 Mỗi người giới thiệu = *+25 điểm* + hoa hồng IB\n"
        "💰 Đăng ký sàn qua link của bạn = *$10–$30* hoa hồng"
    )


def score_message(full_name: str, score: int, ref_count: int) -> str:
    if score < 50:
        rank, bar = "🌱 Tân binh", "▱▱▱▱▱"
    elif score < 150:
        rank, bar = "🥉 Tiềm năng", "▰▱▱▱▱"
    elif score < 300:
        rank, bar = "🥈 Trader Bạc", "▰▰▱▱▱"
    elif score < 500:
        rank, bar = "🥇 Trader Vàng", "▰▰▰▱▱"
    else:
        rank, bar = "💎 Elite Trader", "▰▰▰▰▰"
    return (
        "📊 *ĐIỂM TÍCH LŨY CỦA BẠN*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"👤 {full_name}\n"
        f"⭐ Điểm: *{score} điểm*\n"
        f"🏅 Hạng: *{rank}* {bar}\n"
        f"👥 Giới thiệu: *{ref_count} người*\n\n"
        "📈 *Cách tăng điểm:*\n"
        "   • Xem WOXBOT: +10đ\n"
        "   • Click đăng ký sàn: +15đ\n"
        "   • Giới thiệu thành viên: +25đ\n"
        "   • Xem WOXBIZ: +8đ\n\n"
        "🎁 Tích đủ *100 điểm* để nhận quà từ WOXBAL!"
    )


# ═══════════════════════════════════════════════════════
#  ANTI-SPAM & MODERATION
# ═══════════════════════════════════════════════════════

def spam_warning_message(full_name: str, warn_count: int, max_warns: int = 3) -> str:
    return (
        f"⚠️ *CẢNH CÁO VI PHẠM — {full_name}*\n\n"
        f"Tin nhắn của bạn đã bị xóa do vi phạm nội quy.\n\n"
        f"🔴 Lần cảnh cáo: *{warn_count}/{max_warns}*\n\n"
        f"{'⛔ Lần cuối — Bạn sẽ bị kick ngay vi phạm tiếp theo!' if warn_count >= max_warns - 1 else '❗ Vi phạm tiếp theo có thể dẫn đến bị kick nhóm.'}\n\n"
        "📌 Đọc lại nội quy: /rules"
    )


KICKED_MESSAGE = "⛔ Thành viên đã bị kick do vi phạm nội quy nhóm 3 lần."


# ═══════════════════════════════════════════════════════
#  ADMIN STATS
# ═══════════════════════════════════════════════════════

def admin_stats_message(total: int, top_refs: list, signal_count: int = 0, faq_hits: int = 0) -> str:
    top_list = ""
    for i, r in enumerate(top_refs, 1):
        name = r.get("full_name") or r.get("username") or "N/A"
        top_list += f"   {i}. {name} — {r['total']} người\n"
    return (
        "📊 *THỐNG KÊ WOXHUB*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"👥 Tổng thành viên: *{total}*\n"
        f"📡 Tín hiệu 7 ngày qua: *{signal_count}*\n"
        f"❓ FAQ được giải đáp: *{faq_hits}*\n\n"
        "🏆 *Top người giới thiệu:*\n"
        f"{top_list if top_list else '   Chưa có dữ liệu'}"
    )


# ═══════════════════════════════════════════════════════
#  SIGNALS
# ═══════════════════════════════════════════════════════

def format_signal_message(text: str, source_channel: str = "WOXBOT SIGNAL") -> str:
    return (
        f"📡 *TÍN HIỆU TỪ {source_channel}*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"{text}\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n"
        "⚠️ *Quản lý vốn: Không dùng >2% vốn/lệnh*\n"
        "📊 Kết quả lịch sử không đảm bảo tương lai"
    )


# ═══════════════════════════════════════════════════════
#  SEEDING CONTENT — DAILY
# ═══════════════════════════════════════════════════════

MORNING_BRIEFS = [
    (
        "☀️ *CHÀO BUỔI SÁNG — WOXHUB COMMUNITY!*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "📅 Hôm nay là thứ Hai — Đầu tuần đầy năng lượng!\n\n"
        "🎯 *Focus của ngày:*\n"
        "• Phiên Á đang trong trạng thái tích lũy\n"
        "• London mở lúc *15:00 (GMT+7)* — Cơ hội breakout\n"
        "• XAU/USD cần theo dõi mốc kháng cự\n\n"
        "💡 *Quote ngày hôm nay:*\n"
        "_\"Kỷ luật là cây cầu giữa mục tiêu và thành công.\"_\n\n"
        "📡 Tín hiệu hôm nay sẽ được gửi vào lúc buổi chiều!\n"
        "Chúc anh em giao dịch an toàn! 🚀"
    ),
    (
        "☀️ *CHÀO BUỔI SÁNG — WOXHUB COMMUNITY!*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "📅 Thứ Ba — Tiếp tục bứt phá!\n\n"
        "🎯 *Focus của ngày:*\n"
        "• Dữ liệu kinh tế quan trọng hôm nay\n"
        "• Biến động có thể tăng trong phiên Mỹ\n"
        "• Chú ý quản lý SL kỹ hơn ngày thường\n\n"
        "💡 *Quote ngày hôm nay:*\n"
        "_\"Người thành công không phải là người không thất bại,\nmà là người đứng dậy nhiều hơn số lần ngã.\"_\n\n"
        "📡 Theo dõi tín hiệu WOXBOT để không bỏ lỡ cơ hội!\n"
        "Giao dịch có kế hoạch nhé anh em! 💪"
    ),
    (
        "☀️ *CHÀO BUỔI SÁNG — WOXHUB COMMUNITY!*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "📅 Thứ Tư — Giữa tuần, giữ vững!  \n\n"
        "🎯 *Focus của ngày:*\n"
        "• FOMC minutes/Fed speeches — theo dõi sát\n"
        "• USD có thể biến động mạnh\n"
        "• XAU/USD phản ứng ngược chiều USD\n\n"
        "💡 *Quote ngày hôm nay:*\n"
        "_\"Thị trường thưởng cho sự kiên nhẫn và trừng phạt sự tham lam.\"_\n\n"
        "🗳️ Poll cộng đồng sẽ được gửi hôm nay — Vote nhé!\n"
        "Giao dịch có kiểm soát anh em ơi! 🎯"
    ),
    (
        "☀️ *CHÀO BUỔI SÁNG — WOXHUB COMMUNITY!*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "📅 Thứ Năm — Gần đích cuối tuần rồi!\n\n"
        "🎯 *Focus của ngày:*\n"
        "• ECB/BOE có thể phát biểu — chú ý cặp EUR, GBP\n"
        "• Jobless Claims US — market mover\n"
        "• XAU/USD theo dõi vùng hỗ trợ\n\n"
        "💡 *Quote ngày hôm nay:*\n"
        "_\"Một giao dịch tốt không phải là giao dịch thắng, mà là giao dịch đúng hệ thống.\"_\n\n"
        "📚 Nội dung đào tạo đặc biệt sẽ được chia sẻ tối nay!\n"
        "Chúc anh em một ngày hiệu quả! 🔥"
    ),
    (
        "☀️ *CHÀO BUỔI SÁNG — WOXHUB COMMUNITY!*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "📅 Thứ Sáu — Chốt tuần mạnh mẽ!\n\n"
        "🎯 *Focus của ngày:*\n"
        "• NFP (Non-Farm Payrolls) — Quan trọng nhất tuần!\n"
        "• Biến động cực mạnh vào lúc 19:30 GMT+7\n"
        "• Không nên giữ lệnh qua thời điểm này\n\n"
        "💡 *Quote ngày hôm nay:*\n"
        "_\"Bảo vệ vốn là ưu tiên số 1 — Cơ hội luôn đến sau.\"_\n\n"
        "🏆 Bảng xếp hạng tuần này sẽ cập nhật vào Thứ 2!\n"
        "Chốt tuần an toàn nhé anh em! 🌟"
    ),
]

EVENING_RECAPS = [
    (
        "🌙 *TỔNG KẾT PHIÊN — WOXHUB COMMUNITY*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "📊 Phiên giao dịch hôm nay đã kết thúc.\n\n"
        "💬 *Chia sẻ kết quả của bạn hôm nay:*\n"
        "   ✅ Thắng — React 👍\n"
        "   ❌ Thua — React 👎\n"
        "   ⏳ Đang giữ lệnh — React 🤔\n\n"
        "📌 *Nhớ:* Luôn review lại giao dịch để cải thiện!\n\n"
        "💡 Cần hỗ trợ phân tích? Nhắn admin ngay nhé.\n\n"
        "🔗 Giới thiệu bạn bè để nhận thưởng: /myref\n"
        "Nghỉ ngơi tốt & chuẩn bị cho ngày mai! 😴"
    ),
    (
        "🌙 *TỔNG KẾT PHIÊN — WOXHUB COMMUNITY*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "📊 Một ngày giao dịch nữa đã qua!\n\n"
        "🤔 *Câu hỏi tự vấn mỗi tối:*\n"
        "   • Hôm nay mình đã tuân thủ kế hoạch chưa?\n"
        "   • SL có đặt đúng vị trí không?\n"
        "   • Cảm xúc có ảnh hưởng đến quyết định không?\n\n"
        "💎 *Nhớ:* Trader thành công là người kỷ luật nhất, không phải thắng nhiều nhất.\n\n"
        "🏦 Chưa đăng ký sàn qua link WOXHUB?\n"
        "Đăng ký hôm nay để nhận ngay hoa hồng IB! 👆\n\n"
        "Hẹn gặp lại sáng mai! 🌅"
    ),
]

EDUCATIONAL_SNIPPETS = [
    (
        "📚 *KIẾN THỨC TRADER — WOXHUB EDU*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "🎯 *Quản lý vốn: Quy tắc 1-2%*\n\n"
        "Đây là nguyên tắc sống còn của mọi trader chuyên nghiệp:\n\n"
        "✅ Không bao giờ rủi ro quá *1-2% tổng vốn* trong một lệnh\n"
        "✅ Với vốn $1.000 → tối đa $10–$20/lệnh\n"
        "✅ Ngay cả khi thua 10 lệnh liên tiếp, vốn vẫn còn >80%\n\n"
        "❌ *Lỗi phổ biến:* Dùng 10-20% vốn/lệnh → một lệnh thua = mất nhiều tháng\n\n"
        "💡 WOXBOT được thiết kế theo đúng nguyên tắc này!\n\n"
        "❓ Có câu hỏi về quản lý vốn? Comment bên dưới!"
    ),
    (
        "📚 *KIẾN THỨC TRADER — WOXHUB EDU*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "🎯 *XAU/USD: Tại sao Vàng lại biến động?*\n\n"
        "Vàng (XAU/USD) bị ảnh hưởng bởi:\n\n"
        "📈 *Tăng khi:*\n"
        "   • USD yếu đi\n"
        "   • Lạm phát tăng\n"
        "   • Bất ổn địa chính trị\n"
        "   • Fed giảm lãi suất\n\n"
        "📉 *Giảm khi:*\n"
        "   • USD mạnh lên\n"
        "   • Lãi suất tăng\n"
        "   • Thị trường risk-on\n\n"
        "💡 Hiểu rõ driver = giao dịch có nền tảng!\n"
        "WOXBOT phân tích tất cả yếu tố này tự động.\n\n"
        "👍 Thấy hữu ích? Share cho bạn bè nhé!"
    ),
    (
        "📚 *KIẾN THỨC TRADER — WOXHUB EDU*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "🎯 *IB (Introducing Broker) là gì?*\n\n"
        "IB = người giới thiệu khách hàng cho sàn giao dịch\n"
        "và nhận hoa hồng từ volume giao dịch của họ.\n\n"
        "💰 *Cách IB tạo thu nhập thụ động:*\n"
        "   1. Bạn giới thiệu A đăng ký sàn qua link của bạn\n"
        "   2. A trade 10 lot/tháng\n"
        "   3. Bạn nhận $3–$5/lot × 10 lot = *$30–$50/tháng từ 1 người*\n"
        "   4. Có 20 người = *$600–$1.000/tháng thụ động*\n\n"
        "✅ Không cần trade giỏi mới làm IB được!\n"
        "✅ WOXBAL cung cấp toàn bộ tool & training\n\n"
        "💬 Muốn bắt đầu IB? Nhắn admin ngay!"
    ),
    (
        "📚 *KIẾN THỨC TRADER — WOXHUB EDU*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "🎯 *Stop Loss: Người bạn tốt nhất của Trader*\n\n"
        "Nhiều người mới sợ đặt SL vì \"sợ bị cắt\".\n"
        "Thực tế, *không đặt SL mới là nguy hiểm nhất!*\n\n"
        "✅ *SL tốt = đặt dưới vùng hỗ trợ quan trọng*\n"
        "✅ Tỷ lệ Risk:Reward tối thiểu 1:2\n"
        "✅ Không move SL khi lệnh đang lỗ\n\n"
        "❌ *Sai lầm phổ biến:*\n"
        "   • Không đặt SL → margin call\n"
        "   • Đặt SL quá gần entry → bị hunt\n"
        "   • Move SL ra xa khi đang lỗ\n\n"
        "💡 WOXBOT tự động tính SL dựa trên ATR!\n\n"
        "Bảo toàn vốn là ưu tiên số 1! 🛡️"
    ),
]


# ═══════════════════════════════════════════════════════
#  FAQ RESPONSES
# ═══════════════════════════════════════════════════════

FAQ_RESPONSES = {
    "faq_bot_safe": (
        "🤖 *WOXBOT CÓ AN TOÀN KHÔNG?*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "✅ *An toàn về mặt kỹ thuật:*\n"
        "• Chạy trên MT4/MT5 tại sàn của BẠN — WOXBAL không giữ tiền\n"
        "• Bot không có quyền rút tiền, chỉ mở/đóng lệnh\n"
        "• Toàn bộ vốn luôn trong tài khoản của bạn\n\n"
        "✅ *Track record minh bạch:*\n"
        "• Kết quả được xác minh qua Myfxbook\n"
        "• 10.000+ thành viên đang sử dụng\n\n"
        "⚠️ *Rủi ro thị trường vẫn tồn tại* — không có EA nào 100%\n"
        "nhưng WOXBOT có hệ thống quản lý rủi ro tích hợp sẵn.\n\n"
        "💬 Liên hệ admin để xem track record chi tiết!"
    ),
    "faq_capital": (
        "💰 *VỐN BỐI NHIÊU ĐỂ BẮT ĐẦU?*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "💡 *Khuyến nghị từ WOXBAL:*\n\n"
        "🔵 *SIGNAL (Phù hợp người mới):*\n"
        "   • Vốn tối thiểu: *$100–$200*\n"
        "   • Trade thủ công theo tín hiệu\n\n"
        "🟡 *½ AUTO:*\n"
        "   • Vốn khuyến nghị: *$300–$500*\n"
        "   • Bot hỗ trợ vào lệnh\n\n"
        "🟢 *AUTO FULL:*\n"
        "   • Vốn tối thiểu: *$500*\n"
        "   • Vốn lý tưởng: *$1.000+* để phát huy tối đa\n\n"
        "⚠️ Chỉ dùng tiền nhàn rỗi — không vay để đầu tư!\n\n"
        "💬 Tư vấn cụ thể theo vốn của bạn: Nhắn admin!"
    ),
    "faq_ib": (
        "🤝 *IB HOẠT ĐỘNG NHƯ THẾ NÀO?*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "IB (Introducing Broker) = bạn giới thiệu người khác\n"
        "đăng ký sàn qua link của bạn và nhận hoa hồng.\n\n"
        "📋 *Quy trình đơn giản:*\n"
        "1️⃣ Đăng ký sàn qua link WOXHUB\n"
        "2️⃣ Báo admin ID → được cấp link IB riêng\n"
        "3️⃣ Chia sẻ link IB cho bạn bè\n"
        "4️⃣ Nhận hoa hồng tự động mỗi tháng\n\n"
        "💰 *Thu nhập:*\n"
        "   • $10–$30/người đăng ký\n"
        "   • $2–$5/lot họ giao dịch (thụ động mãi mãi)\n\n"
        "✅ Không cần kỹ năng trading — WOXBAL cung cấp tool!\n\n"
        "💬 Bắt đầu ngay: Nhắn admin!"
    ),
    "faq_winrate": (
        "📊 *WINRATE TÍN HIỆU WOXBOT LÀ BAO NHIÊU?*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "📈 *Thống kê xác minh (Myfxbook):*\n"
        "   • Winrate trung bình: *72–80%*\n"
        "   • Risk:Reward trung bình: *1:1.5 – 1:2.5*\n"
        "   • Drawdown tối đa: *<15%*\n\n"
        "⚠️ *Lưu ý quan trọng:*\n"
        "• Kết quả lịch sử không đảm bảo tương lai\n"
        "• Luôn dùng SL và quản lý vốn đúng cách\n"
        "• Không all-in một lệnh dù tín hiệu có tốt\n\n"
        "🔍 Muốn xem track record đầy đủ?\n"
        "💬 Liên hệ admin để xem Myfxbook live!"
    ),
    "faq_withdraw": (
        "💸 *RÚT TIỀN NHƯ THẾ NÀO?*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Việc rút tiền hoàn toàn do *BẠN tự thao tác* trong\n"
        "tài khoản sàn — WOXBAL không can thiệp.\n\n"
        "📋 *Quy trình rút tiền (Exness):*\n"
        "1️⃣ Đăng nhập tài khoản sàn\n"
        "2️⃣ Vào mục Rút tiền\n"
        "3️⃣ Chọn phương thức (Bank/e-wallet)\n"
        "4️⃣ Điền số tiền & xác nhận\n"
        "5️⃣ Tiền về trong 1–24h\n\n"
        "✅ Exness & ICMarkets hỗ trợ rút qua:\n"
        "   • Chuyển khoản ngân hàng VN\n"
        "   • USDT/Crypto\n"
        "   • Ví điện tử\n\n"
        "💬 Cần hỗ trợ thao tác? Nhắn admin!"
    ),
    "faq_woxbiz": (
        "💎 *THAM GIA WOXBIZ GIÁ BAO NHIÊU?*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "💰 *Học phí WOXBIZ VIP:*\n"
        "   📌 *$150 / 6 tháng*\n"
        "   📌 *$250 / năm* (tiết kiệm $50)\n\n"
        "🔥 *ROI kỳ vọng từ WOXBIZ:*\n"
        "• Hoa hồng $40/người giới thiệu\n"
        "• Chỉ cần 4 người = hoàn vốn 6 tháng\n"
        "• Thành viên active trung bình: *$500–$2.000/tháng*\n\n"
        "✅ *Bao gồm:*\n"
        "• Signal VIP + coaching 1-1\n"
        "• Funnel automation sẵn dùng\n"
        "• Tool AI hỗ trợ\n\n"
        "💬 Đặt chỗ ngay (số lượng có hạn): Nhắn admin!"
    ),
    "faq_setup_bot": (
        "⚙️ *CÀI ĐẶT WOXBOT NHƯ THẾ NÀO?*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "📋 *Yêu cầu cơ bản:*\n"
        "✅ Tài khoản sàn đã đăng ký qua link WOXHUB\n"
        "✅ Phần mềm MT4 hoặc MT5 (tải miễn phí)\n"
        "✅ VPS (khuyến nghị để chạy 24/7)\n\n"
        "🔧 *Các bước cài đặt:*\n"
        "1️⃣ Tải file EA (.ex4/.ex5) từ admin\n"
        "2️⃣ Copy vào thư mục Experts trong MT4/MT5\n"
        "3️⃣ Khởi động lại MT4/MT5\n"
        "4️⃣ Attach EA vào chart XAU/USD M15\n"
        "5️⃣ Cấu hình lot size theo vốn\n\n"
        "💬 Admin sẽ hỗ trợ cài đặt 1-1!\n"
        "Nhắn admin để được hướng dẫn chi tiết."
    ),
}


# ═══════════════════════════════════════════════════════
#  SEEDING MỚI — TĂNG TƯƠNG TÁC CỘNG ĐỒNG
# ═══════════════════════════════════════════════════════

# ── 1. KICK-OFF ĐẦU TUẦN (Thứ 2 / 07:30 VN) ──────────────────────────────────
KICKOFF_WEEK_MESSAGES = [
    (
        "🔥 *KICK-OFF TUẦN MỚI — WOXHUB COMMUNITY!*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "📅 Thứ Hai đã đến — Tuần mới, cơ hội mới!\n\n"
        "🎯 *Mục tiêu tuần này anh em hãy đặt ra:*\n"
        "   💡 Số lệnh tối đa mỗi ngày?\n"
        "   💡 R:R mục tiêu cho từng lệnh?\n"
        "   💡 Vốn tối đa risk mỗi ngày?\n\n"
        "📊 *Thị trường tuần này cần chú ý:*\n"
        "• Phiên Á: Tích lũy, ít biến động\n"
        "• Phiên London: Cơ hội breakout sáng sớm\n"
        "• Phiên Mỹ: Tin tức quan trọng — cẩn thận!\n\n"
        "💬 Reply ngay: *Mục tiêu của bạn tuần này là gì?* 👇\n\n"
        "Chúc cả nhà một tuần giao dịch thành công! 🚀"
    ),
    (
        "⚡ *TUẦN MỚI BẮT ĐẦU — SẴN SÀNG CHƯA?*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Thứ Hai là ngày để *reset* và *set goal* lại!\n\n"
        "🏆 *3 câu hỏi để bắt đầu tuần đúng cách:*\n"
        "1️⃣ Tuần trước bạn học được gì?\n"
        "2️⃣ Sai lầm nào cần tránh tuần này?\n"
        "3️⃣ 1 điều bạn sẽ làm TỐT HƠN?\n\n"
        "📈 *Trader giỏi không phải người không sai —\n"
        "mà là người không sai cùng 1 lỗi 2 lần!*\n\n"
        "💬 Chia sẻ mục tiêu tuần này của bạn bên dưới nhé! 👇\n\n"
        "WOXHUB đồng hành cùng bạn! 💪"
    ),
    (
        "🌅 *CHÀO BUỔI SÁNG THỨ HAI — WOXHUB!*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "🧠 *Mindset trader tuần này:*\n"
        "_\"Không phải thị trường quyết định bạn thắng hay thua —\n"
        "mà chính kỷ luật của bạn mới quyết định điều đó.\"_\n\n"
        "📋 *Checklist trước khi vào lệnh hôm nay:*\n"
        "☐ Xem lịch tin tức kinh tế\n"
        "☐ Xác định vùng hỗ trợ/kháng cự chính\n"
        "☐ Đặt SL/TP trước khi vào\n"
        "☐ Tính % vốn risk tối đa\n\n"
        "💬 *Hôm nay bạn có plan giao dịch chưa?*\n"
        "Reply ✅ nếu đã sẵn sàng! 👇"
    ),
]

# ── 2. NHẮC LIVESTREAM 13H (Hàng ngày / 12:30 VN) ────────────────────────────
LIVESTREAM_REMINDERS = [
    (
        "📡 *LIVESTREAM 13:00 HÔM NAY — ĐỪNG BỎ LỠ!*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "🎙️ *WOXBAL TEAM* sẽ livestream *PLAN GIAO DỊCH*\n"
        "cho buổi chiều/tối hôm nay trong *30 phút nữa!*\n\n"
        "📊 *Nội dung sẽ phân tích:*\n"
        "• Xu hướng XAU/USD phiên chiều\n"
        "• Vùng vào lệnh tiềm năng\n"
        "• Mức SL/TP khuyến nghị\n\n"
        "🔔 Bật thông báo nhóm để không bỏ lỡ!\n\n"
        "Gặp nhau lúc 13:00 anh em nhé! ⏰"
    ),
    (
        "⏰ *CÒN 30 PHÚT NỮA — LIVESTREAM PLAN 13H!*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Hôm nay thị trường có gì hot?\n"
        "🔥 Admin sẽ chia sẻ *nhận định & plan giao dịch*\n"
        "trực tiếp lúc *13:00* hôm nay!\n\n"
        "💡 *Chuẩn bị trước:*\n"
        "• Mở chart XAU/USD\n"
        "• Note lại các mức giá quan trọng\n"
        "• Chuẩn bị câu hỏi cho admin!\n\n"
        "Tham gia để giao dịch có cơ sở hơn! 🎯"
    ),
    (
        "🎯 *NHẮC NHỞ: LIVESTREAM PLAN GIAO DỊCH 13H!*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "📌 Hàng ngày lúc *13:00*, WOXBAL TEAM livestream\n"
        "phân tích thị trường & đưa ra định hướng giao dịch.\n\n"
        "✅ *Tại sao nên xem?*\n"
        "• Hiểu rõ context thị trường trước khi vào lệnh\n"
        "• Học cách phân tích theo phương pháp WOXBAL\n"
        "• Hỏi trực tiếp — admin trả lời live!\n\n"
        "Còn 30 phút nữa — sẵn sàng chưa? 🚀"
    ),
]

# ── 3. NHẮC LỊCH HỌC (19:00 VN — 1h trước buổi học) ─────────────────────────
CLASS_REMINDER_T2 = (
    "🎓 *NHẮC LỊCH HỌC TỐI NAY — THỨ HAI!*\n"
    "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
    "📚 *TRADER TRAINEE* — Buổi học online\n"
    "⏰ *Thời gian:* 20:00 tối nay trên Zoom\n\n"
    "🎯 *Chương trình dành cho:*\n"
    "Người mới muốn trở thành Trader chuyên nghiệp\n"
    "trong *30 ngày* với lộ trình bài bản từ WOXDEMY!\n\n"
    "✅ *Bạn sẽ học được:*\n"
    "• Nền tảng phân tích kỹ thuật từ cơ bản\n"
    "• Quản lý vốn & tâm lý giao dịch\n"
    "• Cách vận hành WOXBOT hiệu quả\n\n"
    "📌 *Còn 1 tiếng nữa* — chuẩn bị vào học nhé!\n"
    "Liên hệ admin để nhận link Zoom! 👆"
)

CLASS_REMINDER_T4 = (
    "🎓 *NHẮC LỊCH HỌC TỐI NAY — THỨ TƯ!*\n"
    "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
    "📚 *FINTECH BUSINESS MASTERY* — Buổi học online\n"
    "⏰ *Thời gian:* 20:00 tối nay trên Zoom\n\n"
    "🎯 *Chương trình dành cho:*\n"
    "Ai muốn xây dựng hệ thống kinh doanh Fintech\n"
    "*1 người vận hành* — tự động hoàn toàn!\n\n"
    "✅ *Bạn sẽ học được:*\n"
    "• Mô hình kinh doanh IB tự động\n"
    "• Xây phễu & hệ thống chăm sóc khách hàng\n"
    "• Tích hợp AI & Bot vào quy trình kinh doanh\n\n"
    "📌 *Còn 1 tiếng nữa* — chuẩn bị vào học nhé!\n"
    "Liên hệ admin để nhận link Zoom! 👆"
)

CLASS_REMINDER_T6 = (
    "🎓 *NHẮC LỊCH HỌC TỐI NAY — THỨ SÁU!*\n"
    "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
    "📚 *FINTECH LEADERSHIP SYSTEM* — Buổi học online\n"
    "⏰ *Thời gian:* 20:00 tối nay trên Zoom\n\n"
    "🎯 *Chương trình dành cho:*\n"
    "Trader muốn bứt phá lên vai trò *nhà lãnh đạo* —\n"
    "xây đội nhóm & hệ thống thu nhập bền vững!\n\n"
    "✅ *Bạn sẽ học được:*\n"
    "• Xây dựng đội nhóm IB hiệu quả\n"
    "• Leadership & kỹ năng quản lý cộng đồng\n"
    "• Hệ thống thu nhập thụ động từ Fintech\n\n"
    "📌 *Còn 1 tiếng nữa* — chuẩn bị vào học nhé!\n"
    "Liên hệ admin để nhận link Zoom! 👆"
)

# ── 4. NHẮC OFFLINE CHỦ NHẬT (Chủ Nhật / 12:00 VN — 2h trước) ───────────────
OFFLINE_REMINDER = (
    "🤝 *NHẮC OFFLINE WOXBAL HÔM NAY — CHỦ NHẬT!*\n"
    "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
    "📍 *Offline trao đổi kinh nghiệm*\n"
    "⏰ *Thời gian:* 14:00 chiều nay\n"
    "📌 *Địa điểm:* Tp. Hồ Chí Minh\n\n"
    "🌟 *Đây là cơ hội để:*\n"
    "• Gặp gỡ anh em trader trực tiếp\n"
    "• Chia sẻ kinh nghiệm & bài học thực chiến\n"
    "• Kết nối với WOXBAL TEAM\n"
    "• Nhận hỗ trợ & tư vấn 1-1\n\n"
    "💬 Ai tham gia hôm nay? *Reaction hoặc reply nhé!* 👇\n"
    "Còn 2 tiếng — đừng bỏ lỡ! 🔥"
)

# ── 5. SPOTLIGHT THÀNH VIÊN (Thứ 4 / 10:00 VN) ───────────────────────────────
SPOTLIGHT_QUESTIONS = [
    (
        "🌟 *SPOTLIGHT THÀNH VIÊN TUẦN NÀY*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Hôm nay WOXHUB muốn lắng nghe *câu chuyện của BẠN!*\n\n"
        "❓ *Câu hỏi tuần này:*\n"
        "_\"Điều gì khiến bạn quyết định bắt đầu giao dịch Forex/Vàng?_\n"
        "_Và bài học đắt giá nhất bạn đã học được là gì?\"_\n\n"
        "💬 Chia sẻ bên dưới — câu chuyện của bạn có thể\n"
        "truyền cảm hứng cho hàng trăm người khác! 👇\n\n"
        "Người chia sẻ hay nhất sẽ được *vinh danh & tặng điểm thưởng!* 🏆"
    ),
    (
        "🌟 *GÓC CHIA SẺ CỘNG ĐỒNG*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Thứ Tư này — mình hỏi thật, anh em trả lời thật! 😄\n\n"
        "❓ *Câu hỏi:*\n"
        "_\"Tuần trước bạn có lệnh nào khiến bạn tự hào không?_\n"
        "_Hoặc lệnh nào bạn rút ra được bài học quý?\"_\n\n"
        "📊 Đừng ngại kể lệnh thua — trader nào cũng có!\n"
        "Chia sẻ thật để cùng nhau học hỏi!\n\n"
        "💬 Reply bên dưới nhé anh em! 👇"
    ),
    (
        "🌟 *HỎI THĂM CỘNG ĐỒNG WOXHUB*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Giữa tuần rồi — cùng check-in nhé! 📋\n\n"
        "❓ *3 câu hỏi nhanh:*\n"
        "1️⃣ Tuần này bạn đang trade với tâm lý như thế nào?\n"
        "   🟢 Tự tin | 🟡 Bình thường | 🔴 Áp lực\n\n"
        "2️⃣ Kết quả nửa tuần: ➕ Lời hay ➖ Lỗ?\n\n"
        "3️⃣ Bạn cần hỗ trợ gì từ cộng đồng không?\n\n"
        "💬 Reply để admin & anh em hỗ trợ bạn! 👇"
    ),
    (
        "🌟 *TRADER SPOTLIGHT — WOXHUB*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Mỗi tuần chúng ta cùng học hỏi từ nhau! 🎓\n\n"
        "❓ *Câu hỏi tuần này:*\n"
        "_\"Nếu có thể quay lại ngày đầu mới bắt đầu trade,_\n"
        "_bạn sẽ nói gì với bản thân mình?\"_\n\n"
        "💡 Không giới hạn — chia sẻ từ 1 câu đến 1 đoạn!\n"
        "Câu trả lời của bạn có thể thay đổi hành trình\n"
        "của ai đó trong nhóm này. 🙏\n\n"
        "💬 Chia sẻ bên dưới nhé! 👇"
    ),
]

# ── 6. CHALLENGE HÀNG TUẦN (Thứ 5 / 09:00 VN) ───────────────────────────────
WEEKLY_CHALLENGES = [
    (
        "🏆 *CHALLENGE TUẦN NÀY — WOXHUB!*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "⚔️ *Thử thách: KỶ LUẬT R:R*\n\n"
        "📋 *Luật chơi:*\n"
        "• Trong tuần này, mỗi lệnh phải có R:R *tối thiểu 1:2*\n"
        "• Chụp màn hình lệnh đã đóng kèm R:R\n"
        "• Gửi screenshot vào nhóm với hashtag *#RR_CHALLENGE*\n\n"
        "🎁 *Phần thưởng cuối tuần:*\n"
        "• 🥇 Ai đạt R:R ≥ 1:2 nhiều lệnh nhất: *+100 điểm & danh hiệu*\n"
        "• 🥈 Top 2-3: *+50 điểm*\n\n"
        "Bắt đầu ngay từ hôm nay! Ai tham gia? 🙋‍♂️\n"
        "Reply *'Tôi'* để đăng ký! 👇"
    ),
    (
        "🏆 *CHALLENGE TUẦN NÀY — WOXHUB!*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "⚔️ *Thử thách: KHÔNG FOMO 5 NGÀY*\n\n"
        "📋 *Luật chơi:*\n"
        "• Không vào lệnh khi chưa có setup rõ ràng\n"
        "• Không chase lệnh khi đã miss entry\n"
        "• Cuối ngày viết 3 dòng nhật ký giao dịch\n"
        "• Gửi nhật ký vào nhóm với hashtag *#NO_FOMO*\n\n"
        "🎁 *Phần thưởng:*\n"
        "• Ai duy trì đủ 5 ngày: Huy hiệu *'Kỷ luật thép'* 🛡️\n"
        "• Bình chọn nhật ký hay nhất: *+100 điểm*\n\n"
        "Thử thách bắt đầu từ HÔM NAY! Tham gia không? 🙋‍♂️"
    ),
    (
        "🏆 *CHALLENGE TUẦN NÀY — WOXHUB!*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "⚔️ *Thử thách: PHÂN TÍCH CHART TUẦN*\n\n"
        "📋 *Luật chơi:*\n"
        "• Chọn 1 cặp tiền/vàng bạn thích\n"
        "• Phân tích xu hướng và đưa ra dự báo cho tuần\n"
        "• Chụp chart + ghi chú vào nhóm hashtag *#WEEK_ANALYSIS*\n"
        "• Cuối tuần so sánh dự báo vs thực tế\n\n"
        "🎁 *Phần thưởng:*\n"
        "• Phân tích chính xác nhất: *+80 điểm & được review bởi admin*\n"
        "• Mọi người tham gia: *+20 điểm* cho effort!\n\n"
        "Ai sẵn sàng thách thức bản thân? 💪\n"
        "Reply hashtag tên cặp bạn chọn bên dưới! 👇"
    ),
    (
        "🏆 *CHALLENGE TUẦN NÀY — WOXHUB!*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "⚔️ *Thử thách: GIỚI THIỆU & WIN*\n\n"
        "📋 *Luật chơi:*\n"
        "• Giới thiệu bạn bè vào WOXHUB tuần này\n"
        "• Người được giới thiệu cần xác nhận nội quy\n"
        "• Dùng link /myref để tracking\n\n"
        "🎁 *Phần thưởng:*\n"
        "• 🥇 Giới thiệu nhiều nhất: *Thưởng đặc biệt từ WOXBAL*\n"
        "• Mỗi người giới thiệu thành công: *+25 điểm tự động*\n"
        "• Top 3 cuối tuần: *Được vinh danh trên nhóm* 🌟\n\n"
        "Lấy link giới thiệu: /myref\n"
        "Bắt đầu ngay! 🚀"
    ),
]

# ── 7. MINI CONTEST / ĐỌC VỊ THỊ TRƯỜNG (Thứ 5 / 20:00 VN) ──────────────────
MINI_CONTEST_MESSAGES = [
    (
        "🎯 *MINI CONTEST: ĐỌC VỊ VÀNG TUẦN TỚI!*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "📊 Ai có khả năng dự đoán thị trường tốt nhất?\n"
        "Hãy thể hiện! Tuần tới *XAU/USD* sẽ:\n\n"
        "🗳️ *Vote bên dưới hoặc reply:*\n"
        "📈 A — *Tăng* (Bullish)\n"
        "📉 B — *Giảm* (Bearish)\n"
        "↔️ C — *Sideway* (Tích lũy)\n\n"
        "🎁 *Ai đoán đúng + có lý do thuyết phục:*\n"
        "→ *+50 điểm* & được admin review phân tích! 🏆\n\n"
        "Kèm phân tích ngắn vào reply để được điểm cao nhé! 📝"
    ),
    (
        "🎯 *MINI CONTEST: AI ĐOÁN ĐÚNG XAU?*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Cuối tuần này, WOXHUB tổ chức mini contest vui!\n\n"
        "❓ *Câu hỏi:* XAU/USD tuần tới sẽ đóng cửa:\n"
        "   A — Cao hơn tuần này 📈\n"
        "   B — Thấp hơn tuần này 📉\n"
        "   C — Gần như tương đương ↔️\n\n"
        "📝 *Cách tham gia:* Reply A/B/C + lý do ngắn\n\n"
        "🎁 *Top 3 đoán đúng & lý do hay nhất:*\n"
        "• +50 điểm mỗi người\n"
        "• Được vinh danh thứ Hai tuần sau 🏆\n\n"
        "Kết quả công bố thứ Hai tới! Vote ngay! 🗳️"
    ),
]

# ── 8. NỘI DUNG NHẸ CUỐI TUẦN (Thứ 7 / 09:00 VN) ────────────────────────────
WEEKEND_VIBE_MESSAGES = [
    (
        "☕ *CHÀO BUỔI SÁNG THỨ BẢY — WOXHUB!*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Cuối tuần rồi — thư giãn một chút nhé anh em! 😊\n\n"
        "📊 *Nhìn lại tuần này:*\n"
        "Bạn cảm thấy thế nào về kết quả giao dịch tuần này?\n\n"
        "   😄 Hài lòng — tuần tốt!\n"
        "   😐 Bình thường — hòa vốn\n"
        "   😤 Chưa ổn — cần cải thiện\n\n"
        "💬 Reply cảm xúc của bạn + 1 điều bạn học được!\n\n"
        "🌟 Dù kết quả thế nào — bạn đang tiến bộ mỗi ngày!\n"
        "Nghỉ ngơi và nạp năng lượng cho tuần tới nhé! 💪"
    ),
    (
        "🌤️ *THỨ BẢY AN LÀNH — WOXHUB COMMUNITY!*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Weekend là thời gian để *học, review và tái nạp năng lượng!*\n\n"
        "📚 *Gợi ý cho cuối tuần:*\n"
        "1️⃣ Review lại toàn bộ lệnh tuần này\n"
        "2️⃣ Đọc lại 1 kiến thức trading bạn còn yếu\n"
        "3️⃣ Xem lại livestream plan của WOXBAL\n"
        "4️⃣ Nghỉ ngơi — không cần trade T7 CN!\n\n"
        "💬 Hôm nay bạn định làm gì?\n"
        "Chia sẻ kế hoạch cuối tuần bên dưới! 👇"
    ),
    (
        "🏖️ *WEEKEND VIBES — WOXHUB!*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Thứ Bảy — thị trường Forex đóng cửa,\n"
        "nhưng não bộ trader không bao giờ nghỉ! 😄\n\n"
        "🎯 *Hôm nay hỏi thăm anh em một câu:*\n"
        "_\"Ngoài trading, bạn có sở thích hay đam mê gì khác không?\"_\n\n"
        "Vì một trader cân bằng cuộc sống sẽ trade tốt hơn!\n"
        "Đừng để trading chiếm 100% tâm trí bạn nhé 😊\n\n"
        "💬 Chia sẻ hobby của bạn bên dưới — mình muốn biết! 👇"
    ),
]

# ── 9. CHUẨN BỊ TUẦN MỚI (Chủ Nhật / 08:00 VN) ──────────────────────────────
SUNDAY_PREP_MESSAGES = [
    (
        "🌅 *CHÀO CHỦ NHẬT — WOXHUB!*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Chủ Nhật là ngày *tổng kết & chuẩn bị* tốt nhất!\n\n"
        "📋 *Checklist trader cuối tuần:*\n"
        "☐ Review journal giao dịch cả tuần\n"
        "☐ Tính win rate & P&L tuần này\n"
        "☐ Xác định vùng giá quan trọng tuần tới\n"
        "☐ Xem lịch kinh tế tuần sau (investing.com)\n"
        "☐ Set mental target cho tuần tới\n\n"
        "📌 *Nhắc nhở:* Offline WOXBAL hôm nay 14h tại HCM!\n"
        "Ai tham gia? Reply bên dưới! 🙋‍♂️\n\n"
        "Chúc cả nhà một Chủ Nhật bình yên! ☀️"
    ),
    (
        "🔄 *RECAP TUẦN & SẴN SÀNG CHO TUẦN MỚI!*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Trader chuyên nghiệp luôn dành Chủ Nhật để *reset!*\n\n"
        "💡 *3 việc quan trọng nhất hôm nay:*\n"
        "1️⃣ *Review* — Tuần này bạn làm tốt gì?\n"
        "2️⃣ *Learn* — Bài học nào cần nhớ cho tuần sau?\n"
        "3️⃣ *Plan* — Mục tiêu cụ thể cho tuần tới?\n\n"
        "📊 *Thị trường tuần tới:* Hãy chú ý lịch tin tức\n"
        "kinh tế quan trọng trên investing.com nhé!\n\n"
        "💬 Share 1 insight từ tuần này bên dưới! 👇\n"
        "Kiến thức chia sẻ là kiến thức nhân đôi! 🌟"
    ),
]

# ── 10. CÂU HỎI TƯƠNG TÁC HÀNG NGÀY (T2-T6 / 10:30 VN) ─────────────────────
DAILY_QUESTIONS = [
    (
        "💬 *HỎI NHANH — WOXHUB!*\n\n"
        "Hôm nay bạn có vào lệnh không?\n\n"
        "📈 Có — đang theo dõi setup\n"
        "⏳ Chưa — chờ cơ hội tốt hơn\n"
        "❌ Không — hôm nay nghỉ trade\n\n"
        "Reply để mình biết nhé! Giao dịch có kế hoạch! 🎯"
    ),
    (
        "💬 *CHIA SẺ NHANH — WOXHUB!*\n\n"
        "Cảm xúc giao dịch của bạn hôm nay?\n\n"
        "😤 Hưng phấn — muốn vào nhiều lệnh\n"
        "😌 Bình tĩnh — chỉ vào khi có setup\n"
        "😰 Áp lực — đang cần gỡ lỗ\n\n"
        "Dù cảm xúc nào — *kỷ luật vẫn là số 1!* 💪\n"
        "Reply bên dưới nhé! 👇"
    ),
    (
        "🎓 *KIẾN THỨC NHANH — TEST BẢN THÂN!*\n\n"
        "Câu hỏi hôm nay:\n"
        "_\"Bạn thường dùng chỉ báo nào để xác nhận xu hướng?\"_\n\n"
        "📊 MA (Moving Average)\n"
        "📊 RSI / MACD\n"
        "📊 Price Action thuần\n"
        "📊 Kết hợp nhiều chỉ báo\n\n"
        "Reply & chia sẻ lý do — cùng học hỏi nhau! 👇"
    ),
    (
        "💬 *CHECK-IN BUỔI SÁNG — WOXHUB!*\n\n"
        "Chào buổi sáng! Hôm nay bạn đã:\n\n"
        "☐ Xem lịch tin tức kinh tế chưa?\n"
        "☐ Xác định xu hướng chính chưa?\n"
        "☐ Set SL/TP trước khi vào lệnh chưa?\n\n"
        "3 cái tick xanh = Trader có kỷ luật! ✅✅✅\n"
        "Bạn đang ở mức mấy tick? Reply nhé! 👇"
    ),
    (
        "🔥 *ĐỘNG LỰC ĐẦU NGÀY — WOXHUB!*\n\n"
        "_\"Thị trường không quan tâm bạn cảm thấy thế nào.\n"
        "Nhưng kỷ luật của bạn sẽ quyết định bạn kiếm được\n"
        "bao nhiêu từ thị trường đó.\"_\n\n"
        "💪 Giao dịch kỷ luật hôm nay!\n"
        "Ai đã ready? Reply '💪' để bắt đầu! 👇"
    ),
    (
        "📊 *HỎI THĂM CỘNG ĐỒNG — WOXHUB!*\n\n"
        "Mọi người đang trade cặp nào nhiều nhất?\n\n"
        "🥇 XAU/USD (Vàng)\n"
        "🥈 EUR/USD\n"
        "🥉 GBP/USD\n"
        "🎯 Khác — reply tên cặp!\n\n"
        "Vote bên dưới để mình thống kê nhé! 📈"
    ),
    (
        "💡 *TIP TRADING NGÀY HÔM NAY:*\n\n"
        "\"Đừng bao giờ risk nhiều hơn *2% vốn* cho 1 lệnh.\n"
        "Dù bạn chắc chắn đến đâu — thị trường luôn có thể\n"
        "làm điều bất ngờ.\"\n\n"
        "✅ Rule 2% giúp bạn:\n"
        "• Tồn tại lâu dài trong thị trường\n"
        "• Không bị xóa tài khoản sau 1 lệnh tệ\n"
        "• Giao dịch không bị chi phối bởi cảm xúc\n\n"
        "Bạn đang risk bao nhiêu % mỗi lệnh? Chia sẻ nhé! 👇"
    ),
]
}
