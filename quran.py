from telebot import *
from requests import *
from random import *
from time import *
from telebot.types import InlineKeyboardMarkup as Mk
from telebot.types import InlineKeyboardButton as btn 
Token = "6271276762:AAFEyFjfi4_2ST8HBfdSOgRZhlBCRtLdfsY"
bot = TeleBot(Token)
user_ch = "-1001288017420" #معرف قناة النشر بدون @
key , dev = Mk() , Mk() 
dev.add(btn(text=" • المطور • ",url="t.me/x99g9") )
key.add(btn(text="• تفعيل النشر التلقائي 🔛 •",callback_data="run"))
key.add(btn(text="• قناة النشر التلقائي  •", callback_data="ch")) 
key.add(btn(text=" • المطور • ",url="t.me/x99g9"))
bk = Mk().add(btn(text="رجوع 🔙",callback_data=0))
@bot.message_handler(commands=['start'])
def start(message):
	tag = f"[{message.from_user.first_name}](tg://settings)"
	text = f'''*أهلا بك عزيزي •* {tag} *• 
في بوت نشر تلقائي لـ آيات القرآن الكريم
يتم نشر الآيات كُل 24 ساعة
# عليك رفع البوت أدمن في قناة النشر التلقائي
مع صلاحية النشر .
ثم تفعيل النشر من الزر أدناه 👇🏻. *'''
	bot.send_message(message.chat.id,text,parse_mode="Markdown",reply_markup=key)
@bot.callback_query_handler(func=lambda call:True)
def x(call):
	h = 2
	if call.data == "ch":
		name_ch = bot.get_chat(f"@{user_ch}").title
		tag_ch = f"[{name_ch}](t.me/{user_ch})"
		info_ch = Mk()
		info_ch.add(btn(text=f"• {name_ch} •",url=f"t.me/{user_ch}")) 
		info_ch.add(btn(text="رجوع 🔙",callback_data="0"))
		bot.edit_message_text(chat_id=call.message.chat.id ,
		message_id=call.message.message_id,
		text = "*•  رابط قناة النشر التلقائي في الزر أدناه 👇🏻 •*" ,parse_mode="Markdown", reply_markup=info_ch)
	if call.data == "0":
			tag = f"[{call.message.from_user.first_name}](tg://settings)"
			text = f'''*أهلا بك عزيزي
في بوت نشر تلقائي لـ آيات القرآن الكريم
يتم نشر الآيات كُل 24 ساعة
# عليك رفع البوت أدمن في قناة النشر التلقائي
مع صلاحية النشر .
ثم تفعيل النشر من الزر أدناه 👇🏻. *'''
			bot.edit_message_text(chat_id=call.message.chat.id ,
		message_id=call.message.message_id,text = text , 
		parse_mode="Markdown",reply_markup=key) 
	if call.data == "run":
		id_ch = bot.get_chat(f"@{user_ch}").id
		bot.answer_callback_query(call.id,"• تم تفعيل النشر التلقائي ✅.  •")
		try:
			for j in range(6236):
				res = get(f"http://api.alquran.cloud/v1/ayah/{str(randint(1,6236))}/ar.abdulsamad").json()
				x = {
					"text":res['data']['text'] , 
					"mp3":res['data']['audio'] ,
					"name":res['data']['surah']['name'] , 
					"part":res['data']['juz'] , 
					"page":res['data']['page'] , 
					"hizb":res['data']['hizbQuarter'] , 
					"ayh":res['data']['numberInSurah'],
					}
				text = f"""
• {x['name']} • \n\n*﴿ {x['text']} ﴾* \n\n- الجزء: {x['part']} - الحزب: {x['hizb']} - الأية: {x['ayh']} - الصفحة: {x['page']} . \nㅤ"""
				bot.send_audio(id_ch,x['mp3'],text, parse_mode="Markdown",reply_markup=dev)
				sleep(86400)
		except:pass
bot.polling(True)
