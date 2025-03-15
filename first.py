from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

Token = "6766817132:AAH8QcVCpLMDMMuOLU92MmyoRL0reu9IpSI"

async def ShowMenu(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    # Reply Keyboard (Visible on chat screen)
    keyboard = [[KeyboardButton("This is first button"), KeyboardButton("This is second button")]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    # Inline Keyboard (Buttons under the message)
    inline_keyboard = [[InlineKeyboardButton("This is inline keyboard", url="https://www.google.com")]]
    inline_markup = InlineKeyboardMarkup(inline_keyboard)

    await update.message.reply_text("Menu", reply_markup=reply_markup)
    await update.message.reply_text("Click below:", reply_markup=inline_markup)

async def Start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo(photo=open("image.png", "rb"), caption="Welcome!")  # Make sure the image exists
    await ShowMenu(update, ctx)

app = ApplicationBuilder().token(Token).build()
app.add_handler(CommandHandler("start", Start))

if __name__ == "__main__":
    print("Bot is running!")
    app.run_polling()
