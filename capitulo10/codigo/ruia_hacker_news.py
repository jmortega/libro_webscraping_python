#!/usr/bin/env python
from ruia import Item, Spider, TextField, AttrField


class HackerNewsItem(Item):
    target_item = TextField(css_select="tr.athing")
    title = TextField(css_select="span.titleline")
    link = AttrField(css_select="span.titleline>a",attr="href")

class HackerNewsSpider(Spider):
    start_urls = ["https://news.ycombinator.com"]

    async def parse(self, response):
        async for item in HackerNewsItem.get_items(html=await response.text()):
        	print(item)
        	yield item


if __name__ == "__main__":
    HackerNewsSpider.start()
