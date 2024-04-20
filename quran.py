import telebot, requests, random
from telebot import types 
token = "6271276762:AAFEyFjfi4_2ST8HBfdSOgRZhlBCRtLdfsY"#توكنك
bot = telebot.TeleBot(token)   
@bot.message_handler(commands=["start"])
def start(message):
    private = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("حصول على صور", callback_data="religious")
    private.add(button)    
    bot.send_photo(message.chat.id,"https://t.me/uiujq/7628",caption="""
✓ 👋 مرحباً بك عزيزي في بوت الصور الدينية 
✓ 🔍 انقر على الزر ادناة لارسال صورة دينية عشوائية
""", reply_markup=private)
@bot.callback_query_handler(func=lambda call: True)
def imagez(call):
    if call.data == "religious":
        voices = "https://t.me/livequrann/" + str(random.randint(7, 276))
        bot.send_photo(call.message.chat.id, voices, caption="""
«« صلي على محمد وال محمد »» 
""")
print("\033[4;35m-"*10)
print("\033[1;33m• اضغط..... /start ")
print("\033[4;35m-"*10)
bot.polling(none_stop=True)
"""
Dev /- @uiujq 
Ch /- @M02MM 
In /- 2024/2/13
"""
