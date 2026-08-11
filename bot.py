import requests
import os

# Secrets check
TOKEN = os.getenv('8913665698:AAHR-Eio4DE3qWqKQ8SpnJiTrpnU_ujs7Ek')
CHAT_ID = os.getenv('8193076289')

def test():
    if not TOKEN or not CHAT_ID:
        print("❌ ERROR: Secrets (Token/ID) nahi mil rahe. Settings check karo!")
        return

    # Price fetch
    try:
        p_res = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
        price = p_res.json()['bitcoin']['usd']
        
        msg = f"🛰️ *GITHUB POWER TEST*\n💰 BTC: ${price}\n✅ Microsoft Server se message aa gaya!"
        
        # Send to Telegram
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        r = requests.post(url, json={"chat_id": CHAT_ID, "text": msg, "parse_mode": "Markdown"})
        
        if r.status_code == 200:
            print("✅ SUCCESS: Telegram pe message chala gaya!")
        else:
            print(f"❌ TELEGRAM ERROR: {r.text}")
            
    except Exception as e:
        print(f"❌ API ERROR: {e}")

if __name__ == "__main__":
    test()
