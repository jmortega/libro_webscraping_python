#!/usr/bin/env python
from ruia import Item, Spider, TextField, AttrField


class PythonItem(Item):
    target_item = TextField(css_select="a.biglink")
    title = TextField(css_select="a.biglink")
    link = AttrField(css_select="a.biglink",attr="href")

class PythonSpider(Spider):
    start_urls = ["https://docs.python.org/3/"]

    async def parse(self, response):
        async for item in PythonItem.get_items(html=await response.text()):
        	print(item)
        	yield item


if __name__ == "__main__":
    PythonSpider.start()
