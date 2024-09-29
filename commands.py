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
        ['Set Reminder'],                     # First row
        ['Send suggestion to developer'],     # Second row
        ['Ask about security'],               # Third row
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    # Send the greeting with buttons
    await update.message.reply_text(greeting, reply_markup=reply_markup)

# Refactored handlers for button responses
async def set_reminder(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("You chose to set a reminder. Please provide the details!")

async def send_suggestion(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Please send your suggestion to the developer!")

async def ask_security(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("What security concerns do you have?")







