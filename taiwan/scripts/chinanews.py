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

df = pd.read_csv("/Users/yenniejun/Documents/code/eugene/coronavirus/taiwan/data/chinanews21000.csv", engine='python')

for index, row in df[21000:].iterrows():
	print(index)

	try:
		if not pd.isnull(row.url):
			req2 = requests.get(row.url)
			soup2 = BeautifulSoup(req2.text, features="lxml")
			text = ' '.join([p.text for p in soup2.find(class_="article-body").findAll("p")]).strip()
			df.loc[index, 'body'] = text
		else:
			print("null")

	except AttributeError:
		print("Attribution Error")
		continue

	# if index % 1000 == 0:
df.to_csv(f"/Users/yenniejun/Documents/code/eugene/coronavirus/taiwan/data/chinanews.csv", index=False)
