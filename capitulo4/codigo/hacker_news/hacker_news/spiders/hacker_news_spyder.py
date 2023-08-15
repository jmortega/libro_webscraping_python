import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from hacker_news.items import HackerNewsItem


class HackerNewsSpyder(Spider):
	name = "hacker_news_spyder"
	allowed_domains = ["news.ycombinator.com"]
	start_urls = ['https://news.ycombinator.com']
	
	def parse(self, response):
		hxs = Selector(response)
		urls = hxs.xpath('//a')
		items = []
		print(urls)
		for url in urls:
			item = HackerNewsItem()
			print(url)
			if url.xpath('text()') is not None and url.xpath('text()') !='' and len(url.xpath('text()').extract())>0:
				item['name'] = url.xpath('text()').extract()[0]
			if url.xpath('@href') is not None and url.xpath('@href') !='' and len(url.xpath('@href').extract())>0:
				item['link'] = url.xpath('@href').extract()[0]
			if not (item['link'].startswith("http")):
				item['link'] ="http://news.ycombinator.com/" +item['link']
			items.append(item)
		return items
