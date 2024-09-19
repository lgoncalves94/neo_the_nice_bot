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


# Function to handle the /complete command
def complete(update: Update, context: CallbackContext) -> None:
   try:
       task_id = int(context.args[0])
       user_id = update.message.from_user.id
       tasks = get_tasks(user_id)
       task_found = False
       for task in tasks:
           if task['id'] == task_id:
               task['status'] = 'Completed'
               task_found = True
               break
       if task_found:
           update.message.reply_text(f"Task {task_id} marked as complete.")
       else:
           update.message.reply_text("Task not found.")
   except (IndexError, ValueError):
       update.message.reply_text("Usage: /complete <task_id>")

# Function to handle the /view command
def view(update: Update, context: CallbackContext) -> None:
   user_id = update.message.from_user.id
   tasks = get_tasks(user_id)
   if tasks:
       response = '\n'.join(
           [f"Task ID: {task['id']} - {task['task_time']} - {task['task_description']} (Status: {task['status']})" for
            task in tasks])
       update.message.reply_text(f"Your tasks:\n{response}")
   else:
       update.message.reply_text("No tasks found.")

# Function to handle the /remove command
def remove(update: Update, context: CallbackContext) -> None:
   if update.message is None:
       update.message.reply_text("Error: No message context available.")
       return
 
 
   try:
       if len(context.args) != 1:
           update.message.reply_text("Usage: /remove <task_id>")
           return
 
 
       task_id = int(context.args[0])
       user_id = update.message.from_user.id
       tasks = get_tasks(user_id)
       task_found = False
 
 
       for task in tasks:
           if task['id'] == task_id:
               tasks_db[user_id] = [t for t in tasks if t['id'] != task_id]
               job_id = f"{user_id}_{task_id}"
               try:
                   scheduler.remove_job(job_id)
               except JobLookupError:
                   logging.warning(f"Job {job_id} not found for removal.")
 
 
               task_found = True
               break
 
 
       if task_found:
           update.message.reply_text(f"Task {task_id} removed successfully.")
       else:
           update.message.reply_text("Task not found.")
   except (IndexError, ValueError) as e:
       logging.error(f"Error in /remove command: {e}")
       update.message.reply_text("Usage: /remove <task_id>")

# Function to handle the /help command
def help(update: Update, context: CallbackContext) -> None:
   help_text = (
       "Here are the commands you can use:\n"
       "/start - Start running the bot and get a welcome message.\n"
       "/add <date> <time> <description> - Add a new timestamped task.\n"
       "/complete <task_id> - Mark a task as completed.\n"
       "/view - View all your tasks.\n"
       "/remove <task_id> - Remove a task.\n"
   )
   update.message.reply_text(help_text)