# 📚 BookFinder Bot (Auto Mode)

This Telegram bot automatically detects and lists all PDF books from the `books/` folder.

## 🚀 Features
- Dynamic menu buttons based on available PDF files
- No need to hard-code book commands
- Easy to scale to 1000s of books
- Built in Python using pyTelegramBotAPI

## 🛠️ Setup on Render
- Build Command: `pip install -r requirements.txt`
- Start Command: `python bot.py`
- Environment Variable: `BOT_TOKEN`

## 📁 Folder Structure
```
mega-book-bot/
├── bot.py
├── requirements.txt
└── books/
    ├── stories/
    │   ├── Lion_and_Mouse.pdf
    │   ├── Greedy_Dog.pdf
    │   └── Tortoise_and_Hare.pdf
    │
    ├── psychology/
    │   ├── Human_Behavior.pdf
    │   ├── Power_of_Mind.pdf
    │   └── Psychological_Tricks.pdf
    │
    ├── historic/
    │   ├── World_War_History.pdf
    │   ├── Islamic_History.pdf
    │   └── Mughal_Empire.pdf
    │
    └── all_subjects/
        ├── Biology_Notes.pdf
        ├── Math_Tricks.pdf
        └── Chemistry_Complete.pdf
```
https://t.me/BookFinderTris_bot
