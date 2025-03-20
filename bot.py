from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters

import os

TOKEN = os.getenv("TOKEN")  # Getting the token from Render

async def start(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("Seller", callback_data="seller"),
         InlineKeyboardButton("Buyer", callback_data="buyer")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome! Are you a Seller or a Buyer?", reply_markup=reply_markup)

async def button_click(update: Update, context):
    query = update.callback_query
    await query.answer()
    role = query.data
    await query.edit_message_text(f"You chose: {role.capitalize()}!")  

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_click))

    print("Bot is running...")  # To check if the bot starts
    app.run_polling()

if __name__ == "__main__":
    main()
