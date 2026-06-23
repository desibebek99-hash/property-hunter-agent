import os
import requests
import feedparser

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

RSS_URLS = os.environ["RSS_URLS"].splitlines()

for rss_url in RSS_URLS:

    print("Membaca:", rss_url)

    feed = feedparser.parse(rss_url)

    print("Jumlah item:", len(feed.entries))

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
