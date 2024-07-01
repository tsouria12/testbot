import os
from flask import Flask
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your bot.')

def main():
    token = os.getenv('TELEGRAM_TOKEN', '6932215235:AAH0L50r7VKtBWYw6OFl7q0DTE_g4l-zLA0')
    port = int(os.environ.get('PORT', '8443'))
    
    updater = Updater(token)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_webhook(listen="0.0.0.0",
                          port=port,
                          url_path=token)
    updater.bot.setWebhook(f"https://testbot-05xl.onrender.com/{token}")

    app.run(host="0.0.0.0", port=port)

    updater.idle()

if __name__ == '__main__':
    main()
 
