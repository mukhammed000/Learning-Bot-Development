from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup

Token = "6766817132:AAH8QcVCpLMDMMuOLU92MmyoRL0reu9IpSI"

async def ShowMenu(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    # keyboard = [[KeyboardButton("This is first button")], [KeyboardButton("This is second button")]] # Vertical
    keyboard = [[KeyboardButton("This is first button"), KeyboardButton("This is second button")]] # Horizontal
    
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text("Menu", reply_markup=reply_markup)

async def Start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo("image.png", caption="Welcome!")
    await ShowMenu(update, ctx)

app = ApplicationBuilder().token(Token).build()
app.add_handler(CommandHandler("start", Start))

if __name__ == "__main__":
    print("Bot is running!")
    app.run_polling()
