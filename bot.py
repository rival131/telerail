import time
import requests
from bs4 import BeautifulSoup
from telegram import Bot

# Ganti dengan token & chat ID Telegram
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

bot = Bot(token=TOKEN)

# Fungsi untuk mendapatkan harga 1B dari website
def get_price():
    url = "https://www.vcgamers.com/gercep/higgs-domino/top-up-game"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Ambil harga dari footer (pastikan selector sesuai)
    price_tag = soup.find("footer")  
    if price_tag:
        return price_tag.text.strip()
    return None

# Simpan harga terakhir
last_price = None

while True:
    current_price = get_price()
    
    if current_price and current_price != last_price:
        message = f"🔥 Harga 1B Koin Emas-D berubah! Sekarang: {current_price}"
        bot.send_message(chat_id=CHAT_ID, text=message)
        last_price = current_price

    time.sleep(60)  # Cek harga setiap 1 menit
