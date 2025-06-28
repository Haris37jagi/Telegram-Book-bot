import telebot
from telebot import types
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

# Categories
CATEGORIES = {
    "English Books": "books/English",
    "Urdu Novels": "books/Novels",
    "Islamic Books": "books/Islamic",
    "Python Books": "books/Python",
    "All Books": "books"
}

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for cat in CATEGORIES:
        markup.add(types.KeyboardButton(cat))
    bot.send_message(message.chat.id, "📚 Welcome to BookFinder Bot!\nPlease choose a category:", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text in CATEGORIES)
def show_books(message):
    folder = CATEGORIES[message.text]
    if not os.path.exists(folder):
        bot.send_message(message.chat.id, "❌ No such category found.")
        return

    books = [f for f in os.listdir(folder) if f.endswith(".pdf")]
    if not books:
        bot.send_message(message.chat.id, "⚠️ No books in this category yet.")
        return

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for b in books:
        markup.add(types.KeyboardButton(f"{message.text} | {b}"))
    markup.add("🔙 Back to Menu")
    bot.send_message(message.chat.id, f"📂 Books in {message.text}:", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text.startswith(tuple(CATEGORIES.keys())))
def send_book(message):
    try:
        category, book_name = message.text.split(" | ")
        folder = CATEGORIES.get(category)
        path = os.path.join(folder, book_name)
        if os.path.exists(path):
            with open(path, "rb") as f:
                bot.send_document(message.chat.id, f)
        else:
            bot.send_message(message.chat.id, "❌ Book not found.")
    except Exception:
        bot.send_message(message.chat.id, "⚠️ Invalid format.")

@bot.message_handler(func=lambda m: m.text == "🔙 Back to Menu")
def go_back(message):
    welcome(message)

print("✅ Bot is running...")
bot.polling()
