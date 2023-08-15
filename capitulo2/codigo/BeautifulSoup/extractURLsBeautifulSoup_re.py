#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import re
import requests
from fake_useragent import UserAgent

ua = UserAgent()
header = {'user-agent':ua.chrome}

url = input("Enter a website to extract the URL's from: ")
response  = requests.get("http://" +url,headers=header)
data = response.text
#print(data)
soup = BeautifulSoup(data,"html.parser")
for link in soup.findAll('a', href=re.compile("^(http|www)")):
    print(link.get('href'))

