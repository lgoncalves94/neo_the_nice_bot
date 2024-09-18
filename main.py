import logging
import pytz
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.base import JobLookupError
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext

# Setup logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Initialize scheduler
scheduler = BackgroundScheduler()
scheduler.start()

# In-memory storage for tasks
tasks_db = {}

# Add tasks
def add_task(user_id,task_time,task_description):
    if user_id not in tasks_db:
        tasks_db[user_id] = []

    task_id = len(tasks_db[user_id] +1)

    tasks_db[user_id].append({
        'id': task_id,
        'task_time':task_time,
        'task_description': task_description,
        'status':'Pending'
        })

# Fetch tasks
def get_tasks(user_id):
    return tasks_db.get(user_id,[])

# Handle /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome to Neo_The_Nice_Bot aka The TaskGod  /add <date> <time> to add a task.')

# Handling add command
def add(update: Update, context: CallbackContext) -> None:
    logging.info(f'Arguments received: {context.args}')

    if len(context.args) < 3 :
        update.message.reply_text('Usage: /add <date> <time> <description>')
        return
    try:
    task_date_str = context.args[0] # Expecting DD-MM-YYYY format
    task_time_str = context.args[1] # Expecting in HH:MM:SS format
    task_description = ' '.join(context.args[2:])
    logging.info(f"Extracted date: {task_date_str}")
    logging.info(f"Extracted time: {task_time_str}")
    logging.info(f"Extracted description: {task_description}")

    task_datetime_str = f"{task_date_str} {task_time_str}"
    task_time = datetime.strptime(task_datetime_str, '%d-%m-%Y %H:%M:%S')

    local_tz = pytz.timezone("Europe/Berlin") # Timezone
    task_time = local_tz.localize(task_time)

    scheduler.add_job(
    send_reminder,
    'date',
    run_date=task_time,
    args=[update.message.chat_id, task_description],
    id=f"{user_id}_{len(tasks_db[user_id])}",
    timezone='Africa/Algiers' # Enter Your Timezone
)

update.message.reply_text(f"Task added for {task_time.strftime('%d-%m-%Y %H:%M:%S')}.")
    except (IndexError, ValueError) as e:
        logging.error(f"Error in /add command: {e}")
        update.message.reply_text("Usage: /add <date> <time> <description>")