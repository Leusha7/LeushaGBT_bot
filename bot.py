from openai import OpenAI
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# შენი გასაღებები
OPENAI_API_KEY = "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"
TELEGRAM_TOKEN = "8469272303:AAERUGhpYyYo7UM3cqTN-Un7XZP-leVeXDk"

# OpenAI კლიენტი
client = OpenAI(api_key=OPENAI_API_KEY)

# ფუნქცია /start სთვის
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("გამარჯობა! მე ვარ შენი პირადი GPT 🤖. მომწერე რამე და გიპასუხებ.")

# ფუნქცია შეტყობინებებზე პასუხისთვის
async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    # GPT პასუხი
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "შენ ხარ მეგობრული ასისტენტი, რომელიც მარტივად ხსნის ყველაფერს."},
            {"role": "user", "content": user_message}
        ]
    )

    bot_reply = response.choices[0].message.content
    await update.message.reply_text(bot_reply)

# აპლიკაციის გაშვება
def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

    print("ბოტი ჩაირთო ✅")
    app.run_polling()

if __name__ == "__main__":
    main()
