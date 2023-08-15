import requests
from bs4 import BeautifulSoup
 
html = requests.get("https://www.python.org")
res = BeautifulSoup(html.text,"html.parser")
tags = res.findAll("h2", {"class": "widget-title"})
for tag in tags:
	print(tag.getText())

