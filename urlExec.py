from concurrent.futures import ThreadPoolExecutor

import requests


wordList = []


with open("extracted_url.txt","r",encoding = "utf-8") as data:
	for i in data:
		wordList.append(i[:-1])
	data.close()
		

def fetch(r,url):

	with r.get(url) as resp2:
		#response = requests.get("https://www.1secmail.com/api/v1/?action=getMessages&login="+i+"&domain=1secmail.com")
			
		print(resp2)


  
if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=10) as executor:
        with requests.Session() as session:
            executor.map(fetch, [session] * len(wordList), wordList)
            executor.shutdown(wait=True)

