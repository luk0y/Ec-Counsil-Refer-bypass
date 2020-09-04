#!/usr/bin/python
# -*- coding: utf-8 -*-

wordList = []

import requests
from concurrent.futures import ThreadPoolExecutor

ids = []
#from bs4 import BeautifulSoup



with open("clean_list.txt","r",encoding = "utf-8") as data:
	for i in data:
		wordList.append(i[:-1])

print(len(wordList))

def fetch(r,wordList):
	global ids
	with r.get("https://www.1secmail.com/api/v1/?action=getMessages&login="+wordList+"&domain=1secmail.com") as resp:
		#response = requests.get("https://www.1secmail.com/api/v1/?action=getMessages&login="+i+"&domain=1secmail.com")
			
		resp_json = resp.json()
		print(resp_json)
		try:
			identifier = resp_json[0]['id']
		
			
			ids.append((identifier,wordList))
		except:
			pass


  
if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=10) as executor:
        with requests.Session() as session:
            executor.map(fetch, [session] * len(wordList), wordList)
            executor.shutdown(wait=True)


file_q = open('id.txt', 'w', encoding='utf-8')

for i in ids:
    file_q.write(str(i) + '\n')

file_q.close()

print("Stage-2 Started")
#State-2 starting from here

extract_urls = []

def fetch(r,id_word):
	global extract_urls
	with r.get("https://www.1secmail.com/mailbox/?action=mailBody&id="+str(id_word[0])+"&login="+id_word[1]+"&domain=1secmail.com") as resp2:
		#response = requests.get("https://www.1secmail.com/api/v1/?action=getMessages&login="+i+"&domain=1secmail.com")
			
		resp2 = resp2.text
	
		url2 = resp2[resp2.find("<a href=\'")+9:resp2.find("\'>Confirm your")]
		
		print(url2)

		extract_urls.append(url2)


  
if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=10) as executor:
        with requests.Session() as session:
            executor.map(fetch, [session] * len(ids), ids)
            executor.shutdown(wait=True)


file_q = open('extracted_url.txt', 'w', encoding='utf-8')

for i in extract_urls:
    file_q.write(i + '\n')

file_q.close()


           
           
           
           
