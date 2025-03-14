from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update

Token = "6766817132:AAH8QcVCpLMDMMuOLU92MmyoRL0reu9IpSI"

async def Start(update: Update, ctx: ContextTypes):
    await update.message.reply_photo("image.png")


app = ApplicationBuilder().token(Token).build()
app.add_handler(CommandHandler("start", Start))

if __name__ == "__main__":
    print("Bot is running! ")
    app.run_polling()
    