#!/bin/bash
# ================================================
#  WOXHUB Bot - Oracle Cloud Server Setup Script
#  Chay 1 lan duy nhat sau khi tao VPS
#  Ubuntu 22.04 LTS
# ================================================

set -e
echo "================================================"
echo "  WOXHUB Bot - Server Setup"
echo "================================================"

# --- Cap nhat he thong ---
echo "[1/6] Cap nhat he thong..."
sudo apt-get update -qq && sudo apt-get upgrade -y -qq

# --- Cai Python 3.11 ---
echo "[2/6] Cai Python 3.11..."
sudo apt-get install -y -qq python3.11 python3.11-venv python3-pip git screen

# --- Tao thu muc bot ---
echo "[3/6] Tao thu muc /opt/woxhub..."
sudo mkdir -p /opt/woxhub
sudo chown ubuntu:ubuntu /opt/woxhub

# --- Tao virtual environment ---
echo "[4/6] Tao Python virtualenv..."
cd /opt/woxhub
python3.11 -m venv venv
source venv/bin/activate

# --- Cai thu vien ---
echo "[5/6] Cai thu vien..."
pip install --quiet --upgrade pip
pip install --quiet "python-telegram-bot[job-queue]==20.7" aiosqlite python-dotenv

# --- Tao systemd service ---
echo "[6/6] Cau hinh auto-start khi reboot..."
sudo tee /etc/systemd/system/woxhub.service > /dev/null <<'EOF'
[Unit]
Description=WOXHUB Telegram Community Bot
After=network.target
Wants=network-online.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/opt/woxhub
ExecStart=/opt/woxhub/venv/bin/python main.py
Restart=always
RestartSec=10
StandardOutput=journal
StandardError=journal
SyslogIdentifier=woxhub

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable woxhub

echo ""
echo "================================================"
echo "  Setup hoan tat!"
echo "  Buoc tiep theo: upload code roi chay deploy.sh"
echo "================================================"
