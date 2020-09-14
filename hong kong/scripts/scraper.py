import urllib.request, urllib.parse
from bs4 import BeautifulSoup
import re
import pandas as pd
import time
import csv
import random
from fake_useragent import UserAgent
import requests
import time
import ast

ua = UserAgent()
fua = ua.random

def getTextSingTao(url):
	try:
	    req = requests.get(url)
	    soup = BeautifulSoup(req.text, 'lxml')
	    body = soup.find("div", class_="paragraphs").text.replace("\n","").replace("\u3000", "").replace("\r", "")
	    if body == "":
	        body = ' '.join([p.text for p in soup.find("div", class_="paragraphs").findAll("p")])
	    body = body.replace("PreviousNext", "").strip()
	    
	    return body
	except:
		print("exception", url)
		return ""

def singTao(s1, e1, s2, e2, search="新冠肺炎"):
	# First time calling
	print("First time calling")
	url = "https://std.stheadline.com/others/%E5%85%B6%E5%AE%83-%E6%90%9C%E5%B0%8B%E5%8F%8A%E7%B5%90%E6%9E%9C"

	startdate = s1
	enddate = e1

	data = {
	    "keyword": search,
	    "section": "all",
	    "subsection": "all",
	    "sd": f'<font style="vertical-align: inherit;"><font style="vertical-align: inherit;">{startdate}</font></font>',
	    "ed": f'<font style="vertical-align: inherit;"><font style="vertical-align: inherit;">{enddate}</font></font>'
	}

	print(data)

	headers = {'User-Agent': fua}
	req = requests.post(url, headers=headers, data=data)
	print(req)
	soup = BeautifulSoup(req.text, 'lxml')

	# First time calling
	print("Getting urls for the first time calling", len(soup.findAll(class_="media-body")))
	urls = []
	titles = []
	dates = []
	bodies = []

	for mb in soup.findAll(class_="media-body"):
	    a = mb.find("a")
	    link = a["href"]
	    title = a["title"]
	    date = mb.find(class_="date").text
	    body = getTextSingTao(link)
	    
	    print(date)

	    urls.append(link)
	    titles.append(title)
	    dates.append(date)
	    bodies.append(body)



	print("subsequent time calling")

	headers = {
	    'User-Agent': fua,
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
	}

	startdate = s2
	enddate = e2

	data = {
	    "keyword": search,
	    "section": "all",
	    "subsection": "all",
	    "sd": f'{startdate}',
	    "ed": f'{enddate}'
	}

	print("Starting to make subsequent calls")

	nextpage = 2

	while True:
	    print("------PAGE", nextpage)
	    url2 = f"https://std.stheadline.com/search/ajax/{nextpage}"
	    cookies = req.cookies

	    req = requests.post(url2, cookies=cookies, headers=headers, data=data)
	    txt = ast.literal_eval(req.text)
	    soup = BeautifulSoup(str(txt), 'lxml')
	    
	    print("len", len(soup.findAll(class_="media-body")))
	    
	    if len(soup.findAll(class_="media-body")) == 0:
	        break

	    index = 0
	    for mb in soup.findAll(class_="media-body"):
	        a = mb.find("a")
	        link = a["href"].replace("\\\\", "");
	        title = a["title"]
	        date = mb.find(class_="date").text
	        date = re.search("\d\d\d\d-\d\d-\d\d", date).group(0)
	        body = getTextSingTao(link)

	        print(index, date)

	        urls.append(link)
	        titles.append(title)
	        dates.append(date)
	        bodies.append(body)
	        index += 1
	        
	    nextpage += 1

	std = pd.DataFrame.transpose(pd.DataFrame([dates, titles, bodies, urls]))
	std.columns = ['date', 'title', 'text', 'url']
	std["source"] = "sing tao daily"
	std["country"] = "hong kong"
	std["keyword"] = search

	std.to_csv(f"/Users/yenniejun/Documents/code/eugene/coronavirus/hong kong/data/singtaodaily{startdate}-{enddate}_{search}.csv")


# singTao("2020/07/01", "2020/07/15", "2020-07-01", "2020-07-15")
# singTao("2020/07/15", "2020/07/31", "2020-07-15", "2020-07-31")
# singTao("2020/06/15", "2020/06/30", "2020-06-15", "2020-06-30")
# singTao("2020/06/01", "2020/06/15", "2020-06-01", "2020-06-15")
# singTao("2020/05/01", "2020/05/15", "2020-05-01", "2020-05-15")
# singTao("2020/05/15", "2020/05/31", "2020-05-15", "2020-05-31")
# singTao("2020/04/15", "2020/04/30", "2020-04-15", "2020-04-30")
# singTao("2020/04/01", "2020/04/15", "2020-04-01", "2020-04-15")

# singTao("2020/02/15", "2020/02/29", "2020-02-15", "2020-02-29")
# singTao("2020/02/01", "2020/02/15", "2020-02-01", "2020-02-15")

# singTao("2020/01/01", "2020/01/31", "2020-01-01", "2020-01-31")
# singTao("2020/01/01", "2020/03/31", "2020-01-01", "2020-03-31", search="covid")
# singTao("2020/04/01", "2020/08/11", "2020-04-01", "2020-08-11", search="covid")
# singTao("2020/03/01", "2020/03/15", "2020-03-01", "2020-03-15")
singTao("2020/03/15", "2020/03/31", "2020-03-15", "2020-03-31")

