#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import sys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

#Example input to enter : en (= english)
convert_from = input("Language to Convert from : ")

#Example input to enter : es (= spanish)
convert_to = input("Language to Convert to : ")

text_to_convert = input("Text to translate: ")

#replace spaces by + symbol
text_to_convert = text_to_convert.replace(' ', '+')

#call translate service
url = 'https://translate.google.com/?sl=%s&tl=%s&text=%s' % (convert_from, convert_to, text_to_convert)

browser = webdriver.Chrome()
browser.get(url)

time.sleep(5)

translation = browser.find_element(By.CLASS_NAME,"er8xn")
translation2 = browser.find_element(By.CLASS_NAME,"QcsUad")
print(translation2.text)

browser.get_screenshot_as_file('google_translate.png')
browser.close()
