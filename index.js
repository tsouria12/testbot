const express = require('express');
const TelegramBot = require('node-telegram-bot-api');
const app = express();
const port = process.env.PORT || 5000;

const token = process.env.TELEGRAM_TOKEN || '6932215235:AAH0L50r7VKtBWYw6OFl7q0DTE_g4l-zLA0';
const bot = new TelegramBot(token, { polling: true });

bot.onText(/\/start/, (msg) => {
  bot.sendMessage(msg.chat.id, 'Hello! I am your bot.');
});

app.get('/', (req, res) => {
  res.send('Hello, World!');
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});

const webhookUrl = `https://testbot-05xl.onrender.com:443/bot${token}`;
bot.setWebHook(webhookUrl);
