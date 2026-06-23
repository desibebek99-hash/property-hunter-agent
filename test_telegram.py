import os
import requests
import feedparser

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]
RSS_URL = os.environ["RSS_URL"]

SENT_FILE = "sent_links.txt"

# baca link yang sudah pernah dikirim
if os.path.exists(SENT_FILE):
    with open(SENT_FILE, "r", encoding="utf-8") as f:
        sent_links = set(line.strip() for line in f)
else:
    sent_links = set()

feed = feedparser.parse(RSS_URL)

new_links = []

for item in feed.entries:

    if item.link in sent_links:
        continue

    pesan = f"""
🏠 Lead Properti Baru

Judul:
{item.title}

Link:
{item.link}
"""

    response = requests.get(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        params={
            "chat_id": CHAT_ID,
            "text": pesan
        }
    )

    print(response.status_code)

    new_links.append(item.link)

# simpan link yang sudah dikirim
if new_links:
    with open(SENT_FILE, "a", encoding="utf-8") as f:
        for link in new_links:
            f.write(link + "\n")

print(f"{len(new_links)} lead baru dikirim")
