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
from os import walk

df = pd.read_csv("/Users/yenniejun/Documents/code/eugene/coronavirus/taiwan/data/uniteddailynews_33000.csv")

for index, row in df[33000:].iterrows():
	print(index)

	try:

		req = requests.get(row.url)
		soup = BeautifulSoup(req.text, features="lxml")

		if soup.find(class_="article-content__editor"):
			text = ' '.join([p.text for p in soup.find(class_="article-content__editor").findAll("p")]).replace('\n', '').replace('\r','').strip()
		else:
			text = ''
			print("Attribute error")
			
		df.loc[index, 'body'] = text

	except ConnectionError:
		print("Connection error")
		continue

	if index % 1000 == 0:
		df.to_csv(f"/Users/yenniejun/Documents/code/eugene/coronavirus/taiwan/data/uniteddailynews_{index}.csv", index=False)

