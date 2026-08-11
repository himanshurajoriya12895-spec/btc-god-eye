import requests, os, time

TOKEN = os.getenv('8913665698:AAHR-Eio4DE3qWqKQ8SpnJiTrpnU_ujs7Ek')
CHAT_ID = os.getenv('8193076289')

def send_tg(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": msg, "parse_mode": "Markdown"})

def get_data():
    # Bybit API use kar rahe hain kyunki ye block nahi hota
    price = float(requests.get("https://api.bybit.com/v5/market/tickers?category=linear&symbol=BTCUSDT").json()['result']['list'][0]['lastPrice'])
    klines = requests.get("https://api.bybit.com/v5/market/kline?category=linear&symbol=BTCUSDT&interval=60&limit=48").json()['result']['list']
    high = max([float(k[2]) for k in klines])
    low = min([float(k[3]) for k in klines])
    
    # Simple Volume Delta logic
    vol = float(requests.get("https://api.bybit.com/v5/market/tickers?category=linear&symbol=BTCUSDT").json()['result']['list'][0]['turnover24h'])
    return price, high, low, vol

price, high, low, vol = get_data()

# LOGIC
if price <= low:
    send_tg(f"🚀 *BEAR TRAP (LONG)*\nPrice: {price}\nSL: {price-150}\nTP: {price+850}")
elif price >= high:
    send_tg(f"🔥 *BULL TRAP (SHORT)*\nPrice: {price}\nSL: {price+150}\nTP: {price-850}")
else:
    print(f"Scanning... Price: {price} | No Signal.")
