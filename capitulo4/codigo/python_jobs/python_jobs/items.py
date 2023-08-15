# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class PythonJobsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    location = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()

