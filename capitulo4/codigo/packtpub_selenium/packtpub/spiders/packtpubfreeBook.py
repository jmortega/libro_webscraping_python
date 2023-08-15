# -*- coding: utf-8 -*-
import scrapy

from time import sleep

import selenium

from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import Request

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

class PacktpubbooksSpider(scrapy.Spider):
	name = "packtpubBooks"
	allowed_domains = ["https://www.packtpub.com/free-learning"]
	start_urls = ('https://www.packtpub.com/free-learning',)
	
	def parse(self, response):
		self.header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}	
		self.driver = webdriver.Chrome()
		self.driver.get('https://www.packtpub.com/free-learning')
		scrapy_selector = Selector(text = self.driver.page_source)
		
		title = scrapy_selector.xpath('/html/body/div[1]/main/header/div/div[1]/div[2]/div/div[2]/div/h3/text()').extract_first()
		yield {'title' : title}


