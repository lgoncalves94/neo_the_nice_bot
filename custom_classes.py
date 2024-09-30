from telegram import Update
from telegram.ext import MessageHandler, filters, CallbackContext
import asyncio



# Listens for neo commands
class NeoCommandHandler(MessageHandler):
    def __init__(self,command,callback):
        command_regex = fr'^neo\s+{command}\b.*'
        super().__init__(filters.Regex(command_regex), callback)


# 104 Greetings
bot_greetings = [
    "Ni hao, {first_name}! This was Chinese! Did you know China is home to the world's oldest continuous written language? Let's make today unforgettable!",  # Chinese
    "Hola, {first_name}! This was Spanish! Spain is home to one of the world’s most unique traditions, the Running of the Bulls in Pamplona! Let’s brighten your day!",  # Spanish
    "Bonjour, {first_name}! This was French! The Louvre Museum in Paris is the world’s largest art museum! I’m here to make your day extra special!",  # French
    "Ciao, {first_name}! This was Italian! Italy’s city of Venice is built entirely on water with over 100 small islands! Let’s make today full of wonders!",  # Italian
    "Hallo, {first_name}! This was German! Germany is known for its castles, with over 20,000 dotted around the country! Let's make this day as grand as one of those!",  # German
    "Привет, {first_name}! This was Russian! Did you know Russia's Trans-Siberian Railway is the longest railway in the world? Let’s embark on a new journey today!",  # Russian
    "こんにちは, {first_name}! This was Japanese! Japan has a festival where you can watch thousands of cherry blossoms bloom called Hanami! Let’s have a beautiful day ahead!",  # Japanese
    "안녕하세요, {first_name}! This was Korean! South Korea’s capital, Seoul, is known as the city that never sleeps! Let’s make today just as lively!",  # Korean
    "Merhaba, {first_name}! This was Turkish! The Grand Bazaar in Istanbul is one of the largest and oldest covered markets in the world! Let’s discover something exciting today!",  # Turkish
    "سلام, {first_name}! This was Arabic! Did you know the first university in the world was founded in Fez, Morocco, and taught in Arabic? Let’s explore new knowledge today!",  # Arabic
    "Olá, {first_name}! This was Portuguese! Brazil’s Amazon rainforest produces 20% of the world’s oxygen! Let’s make today as refreshing as a breath of fresh air!",  # Portuguese
    "Hindi mein aapka swagat hai, {first_name}! This was Hindi! India is home to the world’s largest gathering of people, the Kumbh Mela festival! Let’s make today as magnificent as that!",  # Hindi
    "Kumusta, {first_name}! This was Filipino! Did you know the Philippines has a rice terrace system that is over 2,000 years old? Let’s carve out a great day together!",  # Filipino
    "Hei, {first_name}! This was Norwegian! Norway’s Svalbard has more polar bears than people! Let’s make today truly extraordinary!",  # Norwegian
    "Hallo, {first_name}! This was Dutch! Did you know that the Netherlands is famous for having more bicycles than people? Let’s pedal through this day with ease!",  # Dutch
    "Sveiki, {first_name}! This was Latvian! Latvia’s forests cover more than half the country! Let’s let our ideas grow tall today!",  # Latvian
    "Saluton, {first_name}! This was Esperanto! Esperanto is a constructed international language designed for ease of learning! Let’s build bridges and connect today!",  # Esperanto
    "Ahoj, {first_name}! This was Czech! Did you know that the Czech Republic consumes the most beer per capita in the world? Let’s toast to a fun-filled day ahead!",  # Czech
    "Zdravo, {first_name}! This was Serbian! Serbia’s capital, Belgrade, is one of the oldest cities in Europe! Let’s create something timeless today!",  # Serbian
    "Xin chào, {first_name}! This was Vietnamese! Vietnam has an ancient capital city, Hue, with stunning imperial architecture! Let’s make today as majestic as history itself!",  # Vietnamese
    "Sziasztok, {first_name}! This was Hungarian! Did you know Hungary is home to the largest lake in Central Europe, Lake Balaton? Let’s make today flow smoothly like its waters!",  # Hungarian
    "Salut, {first_name}! This was Romanian! Romania’s Transylvania region inspired the Dracula legend! Let’s dive into something thrilling today!",  # Romanian
    "Shalom, {first_name}! This was Hebrew! Did you know Hebrew was revived as a spoken language after nearly 2,000 years? Let’s make today full of vibrant life!",  # Hebrew
    "Hujambo, {first_name}! This was Swahili! Swahili is famous for its proverbs, like ‘Haraka haraka haina baraka,’ meaning ‘Haste has no blessings!’ Let’s take today step by step!",  # Swahili
    "Tere, {first_name}! This was Estonian! Estonia is known for its digital innovation and was the first country to offer e-Residency! Let’s make today as cutting-edge as possible!",  # Estonian
    "Zdravo, {first_name}! This was Bosnian! Did you know that Bosnia is home to the last remaining jungle in Europe, Perućica? Let’s explore something wild today!",  # Bosnian
    "Mingalaba, {first_name}! This was Burmese! Myanmar is home to the Shwedagon Pagoda, which is believed to be over 2,600 years old! Let’s make today shine just as brightly!",  # Burmese
    "Bonjour, {first_name}! This was Luxembourgish! Luxembourg has the world’s highest GDP per capita! Let’s make today rich in joy and success!",  # Luxembourgish
    "Jó napot, {first_name}! This was Hungarian! Hungary is known for its thermal baths, with over 1,000 hot springs! Let’s soak up today’s opportunities together!",  # Hungarian (alternate)
    "Grüezi, {first_name}! This was Swiss German! Switzerland is famous for its precision watches, like Rolex! Let’s make today perfectly timed and productive!",  # Swiss German
    "Hallo, {first_name}! This was Luxembourgish! Did you know Luxembourg has more Michelin-starred restaurants per capita than any other country? Let’s savor every moment of today!",  # Luxembourgish (alternate)
    "Dzień dobry, {first_name}! This was Polish! Poland is home to Europe’s oldest restaurant, Piwnica Świdnicka, dating back to 1275! Let’s make today feel timeless!",  # Polish
    "Sawubona, {first_name}! This was Zulu! The Zulu language uses unique ‘click’ sounds, part of its rich cultural heritage! Let’s make today just as unique!",  # Zulu
    "Vanakkam, {first_name}! This was Tamil! Tamil is one of the oldest living languages, with a literary tradition spanning over 2,000 years! Let’s write a new chapter today!",  # Tamil
    "Namaste, {first_name}! This was Nepali! Nepal is home to Mount Everest, the highest point on Earth! Let’s aim for new heights today!",  # Nepali
    "Mālō e lelei, {first_name}! This was Tongan! Tonga is one of the only Pacific island nations never colonized! Let’s make today free and full of possibilities!",  # Tongan
    "Sannu, {first_name}! This was Hausa! Did you know Hausa is a tonal language, where the pitch of your voice can change the meaning of words? Let’s tune into today’s excitement!",  # Hausa
    "Selamat siang, {first_name}! This was Indonesian! Indonesia is the world’s largest archipelago, with over 17,000 islands! Let’s explore all the possibilities today!",  # Indonesian
    "Aloha, {first_name}! This was Hawaiian! Hawaii’s Mauna Kea is the tallest mountain in the world when measured from its base underwater! Let’s reach for the stars today!",  # Hawaiian
    "Cześć, {first_name}! This was Polish! Poland is famous for its salt mines, with underground chapels carved from rock salt! Let’s dig deep and uncover greatness today!",  # Polish (alternate)
    "Salve, {first_name}! This was Latin! Did you know that Latin is the root of many languages, including Italian, French, and Spanish? Let’s build something foundational today!",
    "Salamat, {first_name}! This was Tagalog! Did you know the Philippines has more than 7,000 islands, but only about 2,000 are inhabited? Let’s discover something new today!",  # Tagalog
    "Sawubona, {first_name}! This was Zulu! Zulu is known for its rich oral history, passed down through generations! Let’s create something meaningful today!",  # Zulu
    "Moïen, {first_name}! This was Luxembourgish! Luxembourg is one of the world's richest countries and has three official languages! Let’s enrich our day today!",  # Luxembourgish
    "Hola, {first_name}! This was Galician! In Galicia, Spain, there’s a tradition of counting magpies to predict good luck! Let’s make today lucky!",  # Galician
    "Namaste, {first_name}! This was Hindi! Did you know India has the world’s largest postal system, with over 150,000 post offices? Let’s connect as widely as we can today!",  # Hindi
    "Jo napot, {first_name}! This was Hungarian! The Rubik’s Cube was invented by a Hungarian architect, Ernő Rubik! Let’s solve today’s puzzles together!",  # Hungarian (alternate greeting)
    "Kaixo, {first_name}! This was Basque! The Basque language is a linguistic mystery, unrelated to any other language in the world! Let’s explore the unknown today!",  # Basque
    "Hau, {first_name}! This was Lakota! The Lakota people are famous for their role in the American Indian Movement and their enduring resilience! Let’s build strength into today!",  # Lakota
    "Moin, {first_name}! This was Low German! In Northern Germany, ‘Moin’ means both ‘hello’ and ‘goodbye’! Let’s make today a greeting to new opportunities!",  # Low German
    "Tungjatjeta, {first_name}! This was Albanian! Albania is home to the ancient city of Butrint, a UNESCO World Heritage Site! Let’s build something timeless today!",  # Albanian
    "Dumela, {first_name}! This was Setswana! Botswana is home to the world’s largest population of elephants! Let’s make today as majestic as these creatures!",  # Setswana
    "Salam, {first_name}! This was Dari! Afghanistan’s history is filled with legendary empires, from the Silk Road to Alexander the Great! Let’s conquer today’s challenges together!",  # Dari
    "Namaskaram, {first_name}! This was Malayalam! Kerala, where Malayalam is spoken, is known as ‘God’s Own Country’ for its breathtaking landscapes! Let’s create something divine today!",  # Malayalam
    "Sabaidee, {first_name}! This was Lao! Did you know Laos is home to the Plain of Jars, an archaeological wonder? Let’s uncover something mysterious today!",  # Lao
    "Sannu, {first_name}! This was Hausa! Hausa proverbs are rich with wisdom, like ‘A bird will always use its feathers to cover itself.’ Let’s face today with wisdom!",  # Hausa (alternate greeting)
    "Zdravo, {first_name}! This was Bosnian! The city of Sarajevo is where World War I began, changing the course of history forever! Let’s make today’s decisions count!",  # Bosnian
    "Helo, {first_name}! This was Welsh! Wales has more castles per square mile than any other country in Europe! Let’s build a fortress of success today!",  # Welsh
    "Salve, {first_name}! This was Corsican! Corsica is the birthplace of Napoleon Bonaparte! Let’s approach today with the boldness of a conqueror!",  # Corsican
    "Moni, {first_name}! This was Chichewa! Malawi is known as the 'Warm Heart of Africa' because of the friendliness of its people! Let’s make today as warm and welcoming as that!",  # Chichewa
    "Salut, {first_name}! This was Moldovan! Moldova is famous for its underground wine cellars, with some of the largest collections of wine in the world! Let’s uncork something special today!",  # Moldovan
    "Kedu, {first_name}! This was Igbo! The Igbo people are known for their entrepreneurial spirit, which drives innovation! Let’s innovate together today!",  # Igbo
    "Parev, {first_name}! This was Armenian! Armenia was the first country in the world to adopt Christianity as a state religion in 301 AD! Let’s bring light to today’s tasks!",  # Armenian
    "Kamusta, {first_name}! This was Ilocano! Ilocano is spoken by one of the largest ethnolinguistic groups in the Philippines! Let’s make today a shared experience!",  # Ilocano
    "Bula, {first_name}! This was Fijian! Did you know that Fiji has one of the happiest populations on Earth? Let’s make today a joyful one!",  # Fijian (alternate greeting)
    "Shikamoo, {first_name}! This was Swahili (Tanzania)! In Tanzania, Mount Kilimanjaro is the highest peak in Africa! Let’s aim for the summit today!",  # Swahili (Tanzania)
    "Zdravo, {first_name}! This was Montenegrin! Montenegro is known for its dramatic landscapes, with mountains that reach right into the sea! Let’s scale new heights today!",  # Montenegrin
    "Terve, {first_name}! This was Finnish (Karelian)! The Karelian region is known for its unique blend of Finnish and Russian cultures! Let’s blend new ideas today!",  # Karelian
    "Kuzu zangpo la, {first_name}! This was Dzongkha! Bhutan measures its success through Gross National Happiness! Let’s make happiness our goal today!",  # Dzongkha
    "Jó reggelt, {first_name}! This was Hungarian! Did you know that Budapest has the largest thermal water cave system in the world? Let’s dive into something refreshing today!",  # Hungarian (alternate greeting)
    "Asalaam alaikum, {first_name}! This was Wolof! Senegal is famous for its vibrant music scene, including the globally popular Mbalax genre! Let’s create a melody of success today!",  # Wolof
    "Hälsningar, {first_name}! This was Swedish (Åland)! Åland is an autonomous Swedish-speaking region of Finland, known for its peaceful islands! Let’s create tranquility in today’s tasks!",  # Swedish (Åland)
    "Dobry deň, {first_name}! This was Slovak! Slovakia has more than 6,000 caves, making it a true underground wonderland! Let’s explore hidden gems today!",  # Slovak
    "Hola, {first_name}! This was Asturian! The Asturian language is deeply tied to the rugged landscapes of Spain’s northern coast! Let’s weather today’s challenges like a mountain!",  # Asturian
    "Szervusz, {first_name}! This was Hungarian! Hungary boasts some of the most famous thermal baths in Europe! Let’s make today a refreshing experience!",  # Hungarian (alternate greeting)
    "Ahilan, {first_name}! This was Tamil! Tamil is one of the world’s oldest living languages, with literature dating back over 2,000 years! Let’s build on that history today!",  # Tamil
    "Konnichiwa, {first_name}! This was Ainu! The Ainu people of Japan have a unique language and culture, once believed to be unrelated to any other! Let’s celebrate diversity today!",  # Ainu
    "Xin chào, {first_name}! This was Hmong! The Hmong people have no country of their own but maintain their unique cultural identity across Southeast Asia! Let’s make today about resilience!",  # Hmong
    "Mhoro, {first_name}! This was Shona! Zimbabwe’s Great Zimbabwe ruins are an ancient city built entirely without mortar! Let’s build something strong and lasting today!",  # Shona
    "Mingalaba, {first_name}! This was Burmese! Myanmar is home to some of the world's most stunning golden pagodas! Let’s make today shine just as brightly!",  # Burmese (alternate greeting)
    "Bula vinaka, {first_name}! This was Fijian (Rotuman)! The Rotuman people are known for their unique Polynesian culture despite being politically part of Fiji! Let’s embrace uniqueness today!",  # Rotuman
    "Sannu, {first_name}! This was Nupe! The Nupe people of Nigeria are famous for their intricate beadwork and artistry! Let’s craft something beautiful today!",  # Nupe
    "Talofa, {first_name}! This was Samoan! Samoa is famous for its traditional tattoo art, known as ‘pe’a’, a symbol of courage! Let’s be bold today!",  # Samoan
    "Merhaba, {first_name}! This was Kurdish! Did you know the Kurdish region is famous for its epic storytelling traditions? Let’s tell a great story today!",  # Kurdish
    "Xin chào, {first_name}! This was Cham! The Cham people were once part of a powerful maritime empire in Southeast Asia! Let’s navigate today’s seas with skill!",  # Cham
    "Guten Tag, {first_name}! This was Plautdietsch! Plautdietsch is a Low German dialect spoken by Mennonites around the world! Let’s make today globally connected!",  # Plautdietsch
    "Dia dhuit, {first_name}! This was Irish Gaelic! The Irish language has poetic expressions for many everyday things, like ‘mo sheacht mbeannacht’ – my seven blessings! Let’s spread blessings today!",  # Irish Gaelic
    "Mabuhay, {first_name}! This was Kapampangan! Kapampangan is known for its rich culinary traditions, including some of the Philippines' most famous dishes! Let’s cook up something great today!"  # Kapampangan
]




