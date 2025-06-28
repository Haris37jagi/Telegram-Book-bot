## 📚 Available Book Categories (Search Guide)

You can simply **type any keyword** from the book title or category to get matching books.

Here are some examples you can try:

| 🔍 Type This         | 📘 You'll Get Books Like                |
|----------------------|-----------------------------------------|
| `all`                | All subjects: Math, Bio, Physics, etc. |
| `english grammar`    | Basic to advanced grammar PDFs          |
| `stories`            | Moral stories, children's books         |
| `psychology`         | Mental health, human behavior, NLP      |
| `historic`           | Islamic history, world wars, Mughal era |
| `math`               | Short tricks, formulas, MCQs            |
| `biology`            | Diagrams, notes, exam prep              |
| `ielts`              | Listening, speaking, writing modules    |
| `spoken`             | Spoken English, daily phrases           |

### 💬 Example:
Just send:
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
