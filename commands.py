import random
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
        ['Set Reminder'],
        ['Send suggestion to developer'],
        ['Ask about security'],
        ['Get another Greeting']
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
    await update.message.reply_text("Please send your suggestion to the developer!")

async def ask_security(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("""
Yes, your data is securely encrypted!

In our database, we use *Fernet* encryption, which applies a secure symmetric key to protect your data.

We also employ a multi-level key management system, where a primary key encrypts the data
and derived keys are used for additional security.

And these keys are split up among different strongly secured cloud-key providers.

This means that even if one key is compromised, your sensitive information remains protected.

Your privacy and security are our top priorities!""")







