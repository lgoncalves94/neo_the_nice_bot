import random
from datetime import datetime
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import MessageHandler, CallbackContext
from custom_classes import bot_greetings
import asyncio


# Refactored start_command function
async def start_command(update: Update, context: CallbackContext) -> None:
    # Extract data
    user = update.message.from_user
    chat_id = update.message.chat_id
    # Get random greeting
    greeting = random.choice(bot_greetings).format(first_name=user.first_name)
    # Create buttons for user options
    keyboard = [
        ['Set reminder'],
        ['Send suggestion to developer'],
        ['Is my data save?'],
        ['Get another greeting']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    # Send the greeting with buttons
    await update.message.reply_text(greeting, reply_markup=reply_markup)

# Refactored handlers for button responses
async def set_reminder(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("You chose to set a reminder. Please provide the details!")

async def get_greeting(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(random.choice(bot_greetings).format(first_name=update.message.from_user.first_name))

async def send_suggestion(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Please enter your suggestion & if you would like us to get back to you also an e-mail address:")
    # Set a flag indicating we are awaiting the user's suggestion
    context.user_data['awaiting_suggestion'] = True

async def receive_suggestion(update: Update, context: CallbackContext) -> None:
    if context.user_data.get('awaiting_suggestion', False):
        suggestion = update.message.text
        with open("suggestion.txt", "a") as file:
            file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : {suggestion}\n")
        await update.message.reply_text("Thank you for your suggestion!")
        context.user_data['awaiting_suggestion'] = False
    else:
        # If we're not awaiting a suggestion, don't process the input
        await update.message.reply_text("I'm not awaiting any suggestion at the moment.")

async def ask_security(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("""
Yes, your data is securely encrypted!

In our database, we use *Fernet* encryption, which applies a secure symmetric key to protect your data.

We also employ a multi-level key management system, where a primary key encrypts the data
and derived keys are used for additional security.

And these keys are split up among different strongly secured cloud-key providers.

This means that even if one key is compromised, your sensitive information remains protected.

Your privacy and security are our top priorities!""")







