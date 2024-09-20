from utils import *
from datetime import datetime
import pytz
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.base import JobLookupError
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext
  
  
# Initialize scheduler
scheduler = BackgroundScheduler()
scheduler.start()

# Start 
if __name__ == '__main__':
   main()