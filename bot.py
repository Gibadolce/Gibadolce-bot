
import os
import time
from bybit import bybit
import requests

BYBIT_API_KEY = os.getenv("BYBIT_API_KEY")
BYBIT_API_SECRET = os.getenv("BYBIT_API_SECRET")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

client = bybit(test=False, api_key=BYBIT_API_KEY, api_secret=BYBIT_API_SECRET)

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    requests.post(url, data=data)

def run_bot():
    try:
        symbol = "BTCUSDT"
        response = client.Market.Market_symbolInfo().result()
        if response:
            for coin in response[0]['result']:
                if coin['name'] == symbol:
                    price = coin['last_price']
                    send_telegram(f"Prezzo attuale di {symbol}: {price}")
    except Exception as e:
        send_telegram(f"Errore: {str(e)}")

while True:
    run_bot()
    time.sleep(30)
