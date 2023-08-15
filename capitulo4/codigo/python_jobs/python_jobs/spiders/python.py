import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider

from python_jobs.items import PythonJobsItem

class PythonSpider(CrawlSpider):
    name = 'python'
    allowed_domains = ['www.python.org']
    start_urls = ['http://www.python.org/jobs/']
    rules = [Rule(LinkExtractor(allow=('/jobs/'), restrict_css=('.list-recent-jobs')),callback="parse_item", follow=True),]

    def parse_item(self, response):
    	print('Extracting...' + response.url)
    	location = response.css('.text > .listing-company > .listing-location > a::text').extract_first()
    	print(location)
    	title = response.css('.text > .listing-company > .listing-company-name > .company-name::text').extract_first()
    	description = response.xpath('/html/body/div/div[3]/div/section/article/div[1]/p[1]/text()').extract_first()
    	
    	item = PythonJobsItem()
    	item['url'] = response.url
    	if title is not None:
    		title = title.strip()
    		item['title'] = title
    	
    	if description is not None:
    		description = description.strip()
    		item['description'] = description
    	
    	if location is not None:
    		location = location.strip()
    		item['location'] = location
    	
    	yield item
