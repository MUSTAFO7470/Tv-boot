import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Tokeningizni shu yerga yozamiz
TOKEN = "9075976528:AAHJIRkwcRrV0eqDZ3dlkbiBDqntYdwMfVM"
bot = telebot.TeleBot(TOKEN)

# Televizor kanallari ro'yxati va ularning havolalari (video / jonli efir linklari)
CHANNELS = {
    "Uzreport TV": "https://uzreport.uz/livestream",
    "Zo'r TV": "https://zoortv.uz/uz/online",
    "Sevimli TV": "https://sevimli.tv/online",
    "Milliy TV": "https://milliy.tv/live",
    "Sport TV": "https://uzreport.uz/livestream" # misol uchun
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Inline tugmalarni yaratish
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    
    for name, url in CHANNELS.items():
        markup.add(InlineKeyboardButton(name, url=url))
        
    bot.send_message(
        message.chat.id, 
        "📺 **Online Televizorga xush kelibsiz!**\n\nQuyidagi kanallardan birini tanlang va to'g'ridan-to'g'ri onlayn tomosha qiling:", 
        reply_markup=markup,
        parse_mode="Markdown"
    )

print("Bot ishga tushdi...")
bot.infinity_polling()
