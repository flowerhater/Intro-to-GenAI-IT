from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

from bot.translator import ContextTranslator
from bot.config import TELEGRAM_BOT_TOKEN

translator = ContextTranslator()


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("📩 Сообщение отправлено:", update.message.text)
    translated = translator.translate(update.message.text)
    print("📤 Сообщение получено:", translated)
    await update.message.reply_text(translated)



def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Telegram translator bot started")
    app.run_polling()


if __name__ == "__main__":
    main()
