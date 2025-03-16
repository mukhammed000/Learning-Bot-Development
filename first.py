from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from telegram import KeyboardButton, InlineKeyboardButton, ReplyKeyboardMarkup, Update

TOKEN="6766817132:AAH8QcVCpLMDMMuOLU92MmyoRL0reu9IpSI"

async def Menu(upd: Update, ctx: ContextTypes):
    keyboards = [[KeyboardButton("This is first button"), KeyboardButton("This is second button")]]
    reply_keyboard = ReplyKeyboardMarkup(keyboards, resize_keyboard=True)
    
    await upd.message.reply_text("Menu", reply_markup=reply_keyboard)

async def Start(upd: Update, ctx: ContextTypes):
    await upd.message.reply_text("Hello world!")
    await Menu(upd, ctx)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("Start", Start))

if __name__ == "__main__":
    print("Bot is running... ")
    app.run_polling()