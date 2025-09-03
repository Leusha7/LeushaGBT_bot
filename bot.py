from openai import OpenAI
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import logging

# Logging (ფაკულტატიური, მაგრამ კარგი პრაქტიკა)
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# API Keys (Environment Variables)
import os
OPENAI_API_KEY = os.environ.get("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")
TELEGRAM_TOKEN = os.environ.get("8469272303:AAERUGhpYyYo7UM3cqTN-Un7XZP-leVeXDk")

# OpenAI Client
client = OpenAI(api_key=OPENAI_API_KEY)

# /start ფუნქცია
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("გამარჯობა! მე ვარ შენი პირადი GPT 🤖. მომწერე რამე და გიპასუხებ.")

# შეტყობინებების პასუხი
async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "შენ ხარ მეგობრული ასისტენტი."},
            {"role": "user", "content": user_message}
        ]
    )
    bot_reply = response.choices[0].message.content
    await update.message.reply_text(bot_reply)

# Application შექმნა
app = Application.builder().token(TELEGRAM_TOKEN).build()

# Handler-ების დამატება
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

# Global error handler (optional)
async def error_handler(update, context):
    logging.error(msg="Exception while handling an update:", exc_info=context.error)

app.add_error_handler(error_handler)

# ბოტის გაშვება
if __name__ == "__main__":
    app.run_polling()


