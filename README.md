telegram-book-bot/
├── bot.py                ✅ main bot file
├── requirements.txt      ✅ required packages
├── README.md             ✅ GitHub description
└── books/                ✅ put book1.pdf & book2.pdf here
# 📚 BookFinder Bot

This Telegram bot sends free PDF books on command.

## 🤖 Commands

- /start → Welcome message
- /book1 → Sends Book 1 PDF
- /book2 → Sends Book 2 PDF

## 🚀 Hosting (Render.com)

- Build Command: `pip install -r requirements.txt`
- Start Command: `python bot.py`
- Set environment variable: `BOT_TOKEN`

## 📁 Add books in books/ folder
import os
import telebot

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        "📚 Welcome to BookFinder Bot!\n\nUse the commands below to get your free books:\n/book1 – Download Book 1\n/book2 – Download Book 2"
    )

@bot.message_handler(commands=['book1'])
def send_book1(message):
    try:
        with open('books/book1.pdf', 'rb') as book:
            bot.send_document(message.chat.id, book)
    except:
        bot.send_message(message.chat.id, "❌ Book 1 not found.")

@bot.message_handler(commands=['book2'])
def send_book2(message):
    try:
        with open('books/book2.pdf', 'rb') as book:
            bot.send_document(message.chat.id, book)
    except:
        bot.send_message(message.chat.id, "❌ Book 2 not found.")

print("Bot is running...")
bot.polling()
## 🔗 Try the Bot

📲 [Click here to use BookFinder Bot](https://t.me/Bookfindertris_bot)
