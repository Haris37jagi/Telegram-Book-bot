import os
import telebot
from telebot import types

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

BOOK_FOLDER = "books"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    books = [f for f in os.listdir(BOOK_FOLDER) if f.endswith(".pdf")]
    if not books:
        bot.send_message(message.chat.id, "❌ No books found.")
        return

    for book in books:
        markup.add(types.KeyboardButton(book))

    bot.send_message(
        message.chat.id,
        "👋 Welcome to BookFinder Bot (Auto Mode)\n\nChoose a book to download:",
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: message.text.endswith(".pdf"))
def send_selected_book(message):
    book_name = message.text
    book_path = os.path.join(BOOK_FOLDER, book_name)
    if os.path.exists(book_path):
        with open(book_path, 'rb') as book:
            bot.send_document(message.chat.id, book)
    else:
        bot.send_message(message.chat.id, "❌ Book not found.")

print("📚 Auto Book Bot is running...")
bot.polling()
