# api/cron.py — Vercel Cron Handler for WOXHUB Scheduled Jobs
import sys, os, asyncio
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from telegram import Bot

import config
import database as db
import scheduler as sched_module


async def run_job(job_name: str):
    class FakeContext:
        def __init__(self, bot): self.bot = bot

    bot = Bot(config.BOT_TOKEN)
    ctx = FakeContext(bot)
    await db.init_db()

    job_fn = sched_module.JOB_MAP.get(job_name)
    if job_fn:
        await job_fn(ctx)

    await bot.close()


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        params   = parse_qs(urlparse(self.path).query)
        job_name = params.get("job", [""])[0]

        if job_name and job_name in sched_module.JOB_MAP:
            try:
                asyncio.run(run_job(job_name))
                self.send_response(200)
                self.end_headers()
                self.wfile.write(f"Job '{job_name}' OK".encode())
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(f"Error: {e}".encode())
        else:
            self.send_response(400)
            self.end_headers()
            jobs = ", ".join(sched_module.JOB_MAP.keys())
            self.wfile.write(f"Unknown job. Available: {jobs}".encode())

    def log_message(self, fmt, *args):
        pass
