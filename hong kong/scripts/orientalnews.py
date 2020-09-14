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
from datetime import datetime
from time import mktime
from datetime import date
import ast
import json

from datetime import timedelta, date
def daterange(date1, date2):
# https://www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-50.php
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

ua = UserAgent()
fua = ua.random
headers = {'User-Agent': fua, 'Content-Type': 'text/html; charset=utf-8'}

start_dt = date(2020, 1, 1)
end_dt = date(2020, 8, 12)

date_range = []
for dt in daterange(start_dt, end_dt):
    date_range.append(dt)

urls = []
titles = []
dates = []
texts = []

for date in date_range[50:100]:
    print(date)
    url_date = date.strftime("%Y%m%d")
    url = f"https://orientaldaily.on.cc/cnt/news/{url_date}/index.html"
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text.encode('raw_unicode_escape').decode('utf-8'), features="lxml")
    
    print(len(soup.findAll("a")))
    for a in soup.findAll("a")[14:-12]:
        if a.text:
            link = "https://orientaldaily.on.cc" + a["href"]
            title = a.text

            req2 = requests.get(link, headers=headers)
            soup2 = BeautifulSoup(req2.text.encode('raw_unicode_escape').decode('utf-8'), features="lxml")
            body = ' '.join([p.text for p in soup2.findAll("p")])

            if body and "新冠肺炎" in body or "COVID" in body or "covid" in body or "coronavirus" in body:
                urls.append(link)
                titles.append(title)
                texts.append(body)
                dates.append(date)
    
    if len(titles) > 0:
        print("Saving DF for date", url_date)
        df = pd.DataFrame.transpose(pd.DataFrame([dates, titles, texts, urls]))
        df.columns = ['date', 'title', 'text', 'url']
        df['source'] = 'oriental daily news'
        df['keyword'] = "新冠肺炎"
        df["country"] = "hong kong"
        
        df.to_csv(f"/Users/yenniejun/Documents/code/eugene/coronavirus/hong kong/data/chinese/oriental_{url_date}.csv")

