#!/usr/bin/env python3
#scrapy runspider hacker_news_spyder.py -o hacker_news.json

import scrapy
from scrapy import Spider
from scrapy.selector import Selector

class HackerNewsItem(scrapy.Item):
    # define the fields for your item here like
    name = scrapy.Field()
    link = scrapy.Field()

class HackerNewsSpyder(Spider):
    name = "hacker_news_spyder"
    allowed_domains = ["news.ycombinator.com"]
    start_urls = ['https://news.ycombinator.com']
    
    def parse(self, response):
        hxs = Selector(response)
        urls = hxs.xpath('//a')
        items=[]
        print('urls:',urls)
        
        for url in urls:
            item = HackerNewsItem()
            item['name'] = url.xpath('text()').get()
            item['link'] = url.xpath('@href').get()
            if(item['link'].startswith("http")):
                items.append(item)

        return items    
