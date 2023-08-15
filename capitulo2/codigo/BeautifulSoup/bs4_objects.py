#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()
header = {'user-agent':ua.chrome}
google_page = requests.get('http://www.google.com',headers=header)

soup = BeautifulSoup(google_page.content,'lxml')

#find parent
print("Parent of the form with action='/search':")	
parent_form = soup.find("form",{"action":"/search"}).parent
print(parent_form) 

#get children form a specific element,in this case we are getting child elements of the form with action='/search'
print("Children of the form with action='/search'")
for child in soup.find("form",{"action":"/search"}).children:
    print(child)

#find next_siblings	
print("Siblings of the form with action='/search'")
for sibling in soup.find("form",{"action":"/search"}).input.next_siblings:
    print(sibling)
