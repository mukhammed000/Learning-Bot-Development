from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update

TOKEN = "6766817132:AAH8QcVCpLMDMMuOLU92MmyoRL0reu9IpSI"

async def start(update: Update, context: ContextTypes):
    await update.message.reply_text("This is start")

# Create application and add handlers
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

# Run the bot
if __name__ == "__main__":
    print("Bot is running...")
    app.run_polling()