import os
import requests
import feedparser

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

# Untuk sementara satu RSS dulu
RSS_URL = os.environ["RSS_URL"]

feed = feedparser.parse(RSS_URL)

for item in feed.entries[:5]:

    pesan = f"""
🏠 Lead Properti Baru

Judul:
{item.title}

Link:
{item.link}
"""

    r = requests.get(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        params={
            "chat_id": CHAT_ID,
            "text": pesan
        }
    )

    print(r.status_code)

print("Selesai")
