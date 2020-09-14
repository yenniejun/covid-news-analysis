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

ua = UserAgent()
fua = ua.random
headers = {'User-Agent': fua, 'Content-Type': 'text/html; charset=utf-8'}

df = pd.read_csv("/Users/yenniejun/Documents/code/eugene/coronavirus/taiwan/data/libertytimes_457.csv", engine="python")

for index, row in df[457:].iterrows():
    print(index)

    while True:
        req = requests.get(row.url, headers=headers)
        if req.status_code != 200:
            print(req.status_code, "Trying again")
            print(row.url)
            time.sleep(10)
        else:
            break
    
    soup = BeautifulSoup(req.text, features="lxml")
    
    text = ' '.join([p.text.strip() for p in soup.findAll("p")]).replace("\n"," ")
    
    df.loc[index, 'text'] = text

    time.sleep(5)

    if index % 500 == 0:
        df.to_csv(f"/Users/yenniejun/Documents/code/eugene/coronavirus/taiwan/data/libertyimes_{index}.csv", index=False)


    