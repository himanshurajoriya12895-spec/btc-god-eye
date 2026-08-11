import requests
import os
from datetime import datetime

# GitHub Secrets se data lega
TOKEN = os.getenv('8913665698:AAHR-Eio4DE3qWqKQ8SpnJiTrpnU_ujs7Ek')
CHAT_ID = os.getenv('8193076289')

def send_tg(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    try:
        response = requests.post(url, json={"chat_id": CHAT_ID, "text": msg, "parse_mode": "Markdown"})
        print(f"Telegram Response: {response.status_code}")
    except Exception as e:
        print(f"Error sending to Telegram: {e}")

def get_price():
    try:
        # CoinGecko API (GitHub servers ke liye best)
        res = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_24hr_change=true")
        data = res.json()
        price = data['bitcoin']['usd']
        change = data['bitcoin']['usd_24h_change']
        return price, change
    except Exception as e:
        print(f"Error fetching price: {e}")
        return None, None

# --- RUN TESTING ---
price, change = get_price()
now = datetime.now().strftime('%H:%M:%S')

if price:
    emoji = "🟢" if change > 0 else "🔴"
    message = (
        f"🛰️ *GITHUB BOT LIVE TEST*\n\n"
        f"💰 BTC Price: `${price}`\n"
        f"{emoji} 24h Change: `{change:.2f}%`\n"
        f"⏰ Server Time: `{now}`\n\n"
        f"✅ Microsoft Server sahi chal raha hai!"
    )
    send_tg(message)
    print(f"Test Successful: {price}")
else:
    print("Failed to get price.")
