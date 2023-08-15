import scrapy
import selenium
from scrapy.selector import Selector
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.packtpub.com/product/learn-python-programming-third-edition/9781801815093') 

scrapy_selector = Selector(text = driver.page_source)

print(scrapy_selector.xpath('//*[@class="product-info__title"]/text()')[0].get())
