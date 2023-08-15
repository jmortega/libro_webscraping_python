#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import pandas as pd

driver = webdriver.Chrome()

driver.get('https://subscription.packtpub.com/search?query=front%20end%20web%20development')
content = driver.page_source

soup = BeautifulSoup(content,'lxml')

books=[]
authors=[]
descriptions=[]

for element in soup.findAll('div', attrs={'class':'product-card__content'}):
	print(element)
	title = element.find('div', attrs={'class':'product-title mb-3'})
	author = element.find('div', attrs={'class':'product-author'})
	description = element.find('div', attrs={'class':'product-desc mb-3'})
	if title is not None:
		title_text = title.text
	else:
		title_text = ''
	
	if author is not None:
		author_text = author.text
	else:
		author_text = ''
		
	if description is not None:
		description_text = description.text
	else:
		description_text = ''
	
	
	books.append(title_text)
	authors.append(author_text)
	descriptions.append(description_text)
	
df = pd.DataFrame({'Book title':books,'Author':authors,'Description':descriptions})
df.to_csv('books.csv', index=False, encoding='utf-8')
