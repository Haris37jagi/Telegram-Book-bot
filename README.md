# 📚 Mega Book Bot (Auto Mode)

Mega Book Bot is a powerful Telegram bot that allows users to search and download books directly through Telegram. Built with Python and Telebot, it auto-scans the books folder and provides users with an interactive menu to access content easily.

## ✨ Features

- 🔍 Search any book by typing title keywords (e.g. psychology, stories, history, math)
- 📚 Auto-detect all PDF books inside the `books/` folder
- 🧠 Ready to handle thousands or even millions of books (no hardcoding needed)
- 🧾 Commands and buttons auto-generate based on available files
- 🔐 Securely uses environment variable `BOT_TOKEN`
- 🚀 Host on Render.com, Replit, Railway or VPS

## 🗂️ Folder Structure

```
mega-book-bot/
├── bot.py                # Main bot logic
├── requirements.txt      # Required Python packages
├── README.md             # Project documentation (this file)
├── .gitkeep              # Keeps empty folders in git
└── books/                # Upload your PDF books here
    ├── English_Grammar.pdf
    ├── Psychology_101.pdf
    ├── World_History.pdf
    ├── Short_Stories.pdf
    └── AI_Basics.pdf
```

## 🚀 Hosting Instructions (Render.com)

1. Fork or upload this repo to GitHub
2. Go to [Render.com](https://render.com) → New Web Service
3. Connect to GitHub and select this repo
4. Set the following values:
    - **Build Command**: `pip install -r requirements.txt`
    - **Start Command**: `python bot.py`
    - **Environment Variable**: `BOT_TOKEN=your_token_here`
5. Upload your books in the `books/` folder

## 🧪 How to Use

1. Open your bot in Telegram (e.g. [@YourBookBot](https://t.me/YourBookBot))
2. Type `/start` to get the list of available books
3. Or just type part of a book name like `history` or `psychology`

---

👤 Created by Haris