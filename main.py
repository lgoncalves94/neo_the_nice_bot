from telegram.ext  import ApplicationBuilder
from private import BOT_TOKEN
from telegram.ext import ContextTypes, filters, CommandHandler, MessageHandler
from commands import *
from custom_classes import *
import logging
import asyncio

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == '__main__':
    logging.info('Starting the bot...')
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    # Add handlers to the application
    application.add_handler(CommandHandler("start", start_command))
    # Start Buttons
    application.add_handler(MessageHandler(filters.Regex('^Get another greeting$'), get_greeting))
    application.add_handler(MessageHandler(filters.Regex('^Set reminder$'), set_reminder))
    application.add_handler(MessageHandler(filters.Regex('^Send suggestion to developer$'), send_suggestion))
    application.add_handler(MessageHandler(filters.Regex('^Is my data save\\?$'), ask_security))
    application.add_handler(MessageHandler(filters.TEXT, receive_suggestion))
    # Start polling
    logging.info('Bot is running')
    asyncio.run(application.run_polling())