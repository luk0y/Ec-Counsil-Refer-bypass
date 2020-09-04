
"""import requests

import string

import random

import urllib




def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))




head = {

'Host' : 'app.upviral.com',

'Content-Type' : 'application/x-www-form-urlencoded',

'User-Agent':'letmelearn'

}

url = "https://app.upviral.com/embed/request/call/ajax/camp_id/103655/opacity/0.6/widget/iframe/close_popup/no/"



with requests.Session() as r:

	name = id_generator().lower()
	email = name+"@1secmail.com"
	
	email = 'cmongolyat@ll0206.xyzgeneratenewe-mail'

	#postData = '''txt_name=needAllPremiumforFree+'''+id_generator()+'''&txt_email='''+urllib.parse.quote_plus(email)+'''&LeadSource=upviral+referral&agree=agree&reflink=Xs46546963&refshare=&lp_id=&uv_submit=submit'''
	
	postData = '''itemtype=embed&layout=captcha&c=c&txt_name=needAllPremiumforFree+E8FIUO&txt_email='''+urllib.parse.quote_plus(email)+'''&LeadSource=upviral+referral&agree=agree&reflink=Xs46546963&refshare=&lp_id=&uv_submit=submit&opacity=0.6&widget=iframe&close_popup=no&k=0%2F&call=ajax&camp=103655&a=a&captcha=captcha'''
	resp = r.post(url,headers = head,data = postData)
	
	print(resp.text)
	
	resp2 = r.get("https://www.1secmail.com/api/v1/?action=getMessages&login="+name+"&domain=1secmail.com")
	
	print(name)
	
	print(resp2.text)
	
	
	
	
	"""
	
	
#!/usr/bin/python3
# -*- coding: utf-8 -*-

from concurrent.futures import ThreadPoolExecutor

import string

import random

import urllib

import requests

#from bs4 import BeautifulSoup

# from timer import timer

refferal_code = input("Enter your referral code : ")

names = []

url = "https://app.upviral.com/embed/request/call/ajax/camp_id/103655/opacity/0.6/widget/iframe/close_popup/no/"



def fetch(session, url):
	
	global names
	def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
		return ''.join(random.choice(chars) for _ in range(size))
	
	name = id_generator().lower()
	email = name+"@1secmail.com"
	head = {

			'Host' : 'app.upviral.com',

			'Content-Type' : 'application/x-www-form-urlencoded',

			'User-Agent':'letmelearn'

			}
	
	postData = '''itemtype=embed&layout=captcha&c=c&txt_name='''+name+'''&txt_email='''+urllib.parse.quote_plus(email)+'''&LeadSource=upviral+referral&agree=agree&reflink='''+refferal_code+'''&refshare=&lp_id=&uv_submit=submit&opacity=0.6&widget=iframe&close_popup=no&k=0%2F&call=ajax&camp=103655&a=a&captcha=captcha'''

	with session.post(url,headers = head,data = postData) as response:
	
		print(response.text)
				
		names.append(name)


# @timer(1, 5)

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=4) as executor:
        with requests.Session() as session:
            executor.map(fetch, [session] * 500, [url] * 500)
            executor.shutdown(wait=True)
names = sorted(set(names))

file_q = open('clean_list.txt', 'w', encoding='utf-8')

for i in names:
    file_q.write(i + '\n')

file_q.close()

