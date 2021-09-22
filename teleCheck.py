import time, requests, webbrowser
import sys as n
import time as mm
r = requests.session()
def slow(M):
	for c in M + '\n':
		n.stdout.write(c)
		n.stdout.flush()
		mm.sleep(1. / 80)
te = 'By @vv1ck'
print("""
 ██████  ██   ██  █████ 
██@vv1ck ██   ██ ██   ██ 
██ JOKER ███████ ███████ ┌─┐ ┌─┐ ┬┌─ ┬─┐  
██       ██   ██ ██   ██ ├┤  │   ├┴┐ ├┬┘  
 ██████  ██   ██ ██   ██ └─┘ └─┘ ┴ ┴ ┴└─  
            TELEGRAM USERNAME""")
print("""
[1] >> For Arabic Press 1
[2] >> For English Press 2
""")
vv1ck = input('Put the number >> ')
if vv1ck == '1':
	webbrowser.open('https://t.me/vv1ck')
	slow('      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	print('يجب وضع اليوزرات في ملف باسم user.txt')
	print('                               ↓↓↓')
	print('[>] ضع ايدي حسابك : ')
	ID = input(' ')
	print('[>] ضع توكن بوتك : ')
	token = input(' ')
	time.sleep(1.7)
	slow('      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	sl = 'user.txt'
	print(' ')
	m = """
	[☑️] TELEGRAM USER :
	"""
	def tle():
		j = 1
		file = open(sl, 'r')
		while True:
			user = file.readline().split('\n')[0]
			
			if user == '':
				break
			url = f"https://t.me/{user}"
			req = r.get(url)
			if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:	
				print(f"  [{j}] متاح     >> [ {user} ]")
				try:
					req = r.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={m}\n[+] user >> [ @{user} ]\n\n{te}')
				except NameError:
					pass
				with open('Available.txt', 'a') as x:
					tl = '[] NEW USER -->  '
					x.write(tl + user + '\n')
			
			else:
				print(f"  [{j}] غير متاح >> [ {user} ]")				
			j += 1
			time.sleep(1)		
	tle()
# مالك شغل 
elif vv1ck == '2':
	webbrowser.open('https://t.me/vv1ck')
	slow('      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	print('Accounts should be placed in a file named user.txt')
	print('    ↓↓↓')
	print('[>] Enter your ID : ')
	ID = input(' ')
	print('[>] Enter Token bot : ')
	token = input(' ')
	time.sleep(1.7)
	slow('      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	sl = 'user.txt'
	print(' ')
	m = """
	[☑️] TELEGRAM USER :
	"""
	def tle():
		j = 1
		file = open(sl, 'r')
		while True:
			user = file.readline().split('\n')[0]
						
			if user == '':
				break		
			url = f"https://t.me/{user}"
			req = r.get(url)
			if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:
				
				print(f"  [{j}] Available     >> [ {user} ]")
				try:
					req = r.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={m}\n[+] user >> [ @{user} ]\n\n{te}')
				except NameError:
					pass
				
				with open('Available.txt', 'a') as x:
					tl = '[] NEW USER -->  '
					x.write(tl + user + '\n')
				
			else:
				print(f"  [{j}] Not Available >> [ {user} ]")				
			j += 1	
			time.sleep(1)
		
	tle()
# مالك شغل 

else:
	print('      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	print('              الرقم غلط يا ذكي ..   ')
	print('              wrong number')
	print('        By joker / insta : 221298')
