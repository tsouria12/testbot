import os
import logging
from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Logging configuration
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

def start(update: Update, context: CallbackContext) -> None:
    logger.info("Received /start command")
    update.message.reply_text('Hello! I am your bot.')

def run_flask():
    port = int(os.environ.get('FLASK_PORT', '5000'))
    app.run(host="0.0.0.0", port=port)

def run_telegram_bot():
    token = os.getenv('TELEGRAM_TOKEN', '6932215235:AAH0L50r7VKtBWYw6OFl7q0DTE_g4l-zLA0')
    updater = Updater(token)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_webhook(listen="0.0.0.0",
                          port=8443,
                          url_path=token)
    webhook_url = f"https://testbot-05xl.onrender.com/{token}"
    updater.bot.setWebhook(webhook_url)

    updater.idle()

if __name__ == '__main__':
    Thread(target=run_flask).start()
    Thread(target=run_telegram_bot).start()
