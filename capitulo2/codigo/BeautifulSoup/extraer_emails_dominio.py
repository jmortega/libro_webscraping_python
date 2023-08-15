#!/usr/bin/env python3

import requests
import re
from bs4 import BeautifulSoup

url = input("Introduzca la URL: ")
response = requests.get(url)
html_page = response.text
soup = BeautifulSoup(html_page,'lxml')
email_pattern=re.compile(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+')
for match in soup.find_all('a', {'href': email_pattern}):
	print(match['href'])

