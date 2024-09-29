from telegram import Update
from telegram.ext import MessageHandler, filters, CallbackContext
import asyncio



# Listens for neo commands
class NeoCommandHandler(MessageHandler):
    def __init__(self,command,callback):
        command_regex = fr'^neo\s+{command}\b.*'
        super().__init__(filters.Regex(command_regex), callback)


# Greetings


bot_greetings = [
    "Ni hao, {first_name}! This was Chinese! How can I help you today?",  # Chinese
    "Hola, {first_name}! This was Spanish! What can I do for you today?",  # Spanish
    "Bonjour, {first_name}! This was French! How are you today?",  # French
    "Ciao, {first_name}! This was Italian! What’s up today?",  # Italian
    "Hallo, {first_name}! This was German! How's it going today?",  # German
    "Привет, {first_name}! This was Russian! What’s on your mind today?",  # Russian
    "こんにちは, {first_name}! This was Japanese! Ready to learn something today?",  # Japanese
    "안녕하세요, {first_name}! This was Korean! How can I assist you today?",  # Korean
    "Merhaba, {first_name}! This was Turkish! Let’s have some fun today!",  # Turkish
    "سلام, {first_name}! This was Persian! What can I help you with today?",  # Persian
    "Hei, {first_name}! This was Norwegian! Are you excited for today?",  # Norwegian
    "Sveiki, {first_name}! This was Latvian! How are you feeling today?",  # Latvian
    "Ahoj, {first_name}! This was Czech! Ready to get started?",  # Czech
    "Zdravo, {first_name}! This was Serbian! What do you want to explore today?",  # Serbian
    "Xin chào, {first_name}! This was Vietnamese! Let’s dive into something fun!",  # Vietnamese
    "Sziasztok, {first_name}! This was Hungarian! What’s the plan for today?",  # Hungarian
    "Olá, {first_name}! This was Portuguese! Let’s have an amazing day!",  # Portuguese
    "Hej, {first_name}! This was Swedish! Are you ready for an adventure?",  # Swedish
    "Hallå, {first_name}! This was Swedish! How about we learn something new?",  # Swedish (alternate)
    "Szia, {first_name}! This was Hungarian! Let’s make today awesome!",  # Hungarian (alternate)
    "Hujambo, {first_name}! This was Swahili! What are we going to do today?",  # Swahili
    "Tere, {first_name}! This was Estonian! Let’s get started on something exciting!",  # Estonian
    "Kumusta, {first_name}! This was Filipino! What do you want to talk about?",  # Filipino
    "Merhba, {first_name}! This was Maltese! Let’s have a fun conversation!",  # Maltese
    "Salut, {first_name}! This was Romanian! How’s your day going?",  # Romanian
    "Aloha, {first_name}! This was Hawaiian! Ready to explore together?",  # Hawaiian
    "Shalom, {first_name}! This was Hebrew! Let’s learn something today!",  # Hebrew
    "Salam, {first_name}! This was Arabic! What would you like to learn?",  # Arabic
    "Sannu, {first_name}! This was Hausa! Are you ready for some fun?",  # Hausa
    "Ola, {first_name}! This was Portuguese! What can I help you with?",  # Portuguese (alternate)
    "Dobrý den, {first_name}! This was Czech! Let’s have a great time!",  # Czech (alternate)
    "Konnichiwa, {first_name}! This was Japanese! Let’s start an adventure!",  # Japanese (alternate)
    "Merhaba, {first_name}! This was Turkish! What’s the next thing we’ll do?",  # Turkish (alternate)
    "Salve, {first_name}! This was Latin! Ready to explore with me?",  # Latin
]


