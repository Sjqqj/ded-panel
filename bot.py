import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from flask import Flask

TOKEN = os.environ["BOT_TOKEN"]

app = Flask(__name__)

@app.get("/")
def home():
    return "DED PANEL ONLINE"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 پنل دد پوینت آنلاین شد!\n\n"
        "برای شروع مدیریت، /panel رو بزن."
    )

async def panel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👑 پنل مدیریت\n\n"
        "🛠 در حال ساخت..."
    )

def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("panel", panel))

    port = int(os.environ.get("PORT", 10000))

    application.run_webhook(
        listen="0.0.0.0",
        port=port,
        webhook_url=os.environ.get("WEBHOOK_URL")
    )

if __name__ == "__main__":
    main()
