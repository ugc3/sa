
import time
import requests
import telebot
from time import sleep
token = "5573895998:AAHgCJScV49aeQbA5qcW4NM0WrrkyXKP0S4"
bot = telebot.TeleBot(token)
@bot.message_handler(commands = ['greet','start'])
def start(message):
	msg=(f"اهلا بك عزيزي المستخدم هذا البوت مخصص لاستخراج الكوكيز والسيشن ايدي \n\nThe number of bot users reached #1k subscribers Thank you everyone\n\n@MVMVP - @W_Y67")
	bot.send_message(message.chat.id, msg)
	sleep(2)
	bot.send_message(message.chat.id, f"Send User and Password - ارسل اليوزر والباسورد\n\n\r                   user:password")
	
	@bot.message_handler(func=lambda followinG:True )
	
	def com(message):
		uuss = str(message.text)
		username= uuss.split(':')[0]
		password=uuss.split(':')[1]
		url ="https://www.instagram.com/accounts/login/ajax/"
		head1 = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6',
        'content-length': '319',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'mid=YrX_FwABAAFVRYLepbLqUSO9nyBK; ig_did=B86D9D0C-8059-4D38-AB32-62F66F91EB8A; ig_nrcb=1; shbid="6887\054479320179\0541687630562:01f72f17d27d1bf82c5011a7e21c360468f4e96ffc8c8d9bc8f3389196b275ab0b6d598c"; shbts="1656094562\054479320179\0541687630562:01f75b9e3dad31375f7599a21ee1e6b0b33b430c850ee605a7591dd83682126848a683cd"; dpr=3; datr=av-1Yj1HLbt2sRgtjJ2hIyTk; rur="ASH\054479320179\0541687707865:01f7969a9a044b6e5a39c124177ea698ce171408d797be83e4e94e6efc69642ea3b90ed9"; csrftoken=QZnASSTl4lB3b1sG610j7UGrPk0TfrN0',#كوكيز مهمة جداا
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; JSN-L22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
        'viewport-width': '360',
        'x-asbd-id': '437806',
        'x-csrftoken': 'QZnASSTl4lB3b1sG610j7UGrPk0TfrN0',
        'x-ig-app-id': '1217981644879628',
        'x-ig-www-claim': 'hmac.AR2oFTCuitCzXvttHXW3DD1kZLwzL7oauskQL1Jp6ogO6FF6',
        'x-instagram-ajax': '57ac339ce6f4',
        'x-requested-with': 'XMLHttpRequest'
		}
		tim = str(time.time()).split('.')[1]#الوقت اليوم لكن في الاعداد العشرية
		data1 = {
        'username': username,
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{tim}:{password}',
        'queryParams': '{}',
        'optIntoOneTap': 'false',
        'trustedDeviceRecords': '{}'
		}
		rq = requests.post(url,headers=head1,data=data1)
		if ('"userId"') in rq.text:
			co = rq.cookies
			coo =co.get_dict()
			tok = coo['sessionid']
			cookiee = f"sessionid={coo['sessionid']};ds_user_id={coo['ds_user_id']};csrftoken={coo['csrftoken']}"
			bot.send_message(message.chat.id,f"Login True - تسجيل صحيح ✅..\nUsername : {username}\nPassword : {password}\n\n#Cookies - كوكيز\n\n{cookiee}\n\n#Sessionid - سيشن ايدي\n\n{tok}\n\n\n@W_Y67 - @MVMVP")
		elif ('"checkpoint_required"') in rq.text:
				bot.send_message(message.chat.id,f"The Account Scuer of instagram - هذا الحساب سكيور\n\nUsername : {username}\nPassword : {password}\n\n@W_Y67 - @MVMVP")
		elif ('"Please wait a few minutes before you try again."') in rq.text:
			bot.send_message(message.chat.id,f"Time Sleep - الحساب محظور من تسجيل الدخول \nUsername : {username}\nPassword : {password}\n\n@W_Y67 - @MVMVP")
		elif ('"two_factor_required"') in rq.text:
			bot.send_message(message.chat.id,f"Phone Number - مصادقة ثنائية\nUsername : {username}\nPassword : {password}\n\n@W_Y67 - @MVMVP")
			
		else:
				bot.send_message(message.chat.id,f"- No Password False - كلمة السر غير صحيحة\n\nUsername : {username}\nPassword : {password}\n\n@W_Y67- @MVMVP")
				
while True:
	try:
		bot.polling(none_stop=True)
	except Exception as e:
	       print(e)
	       sleep(10)
