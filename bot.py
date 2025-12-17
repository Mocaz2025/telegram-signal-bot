import requests
import time
import os

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": text
    }
    requests.post(url, data=data)

while True:
    send_message(
        "✅ MOCaZ SIGNAL BOT IPO LIVE\n"
        "Bot ina-run 24/7 kupitia Railway.\n"
        "Signal za Boom & Crash zitaanza hivi karibuni."
    )
    time.sleep(3600)
