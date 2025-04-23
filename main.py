
import telepot
import time
import os

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

bot = telepot.Bot(TELEGRAM_BOT_TOKEN)

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        if msg['text'] == "/start":
            bot.sendMessage(chat_id, "Gibadolce è attivo!")

bot.message_loop(handle)
print("Bot Telegram avviato...")

# Loop infinito per mantenere il bot attivo su Render
while True:
    time.sleep(10)
