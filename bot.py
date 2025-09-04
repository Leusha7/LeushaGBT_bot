import os
import logging
from openai import OpenAI
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

# Keys from Environment
OPENAI_API_KEY = os.environ.get("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")
TELEGRAM_TOKEN = os.environ.get("8469272303:AAERUGhpYyYo7UM3cqTN-Un7XZP-leVeXDk")

client = OpenAI(api_key=OPENAI_API_KEY)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("გამარჯობა! მე ვარ შენი უფასო GPT ბოტი 🤖.")

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # უფასო კრედიტისთვის იაფი მოდელი
        messages=[
            {"role": "system", "content": "შენ ხარ მეგობრული ასისტენტი."},
            {"role": "user", "content": user_message}
        ]
    )
    await update.message.reply_text(response.choices[0].message.content)

app = Application.builder().token(TELEGRAM_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

if __name__ == "__main__":
    app.run_polling()



