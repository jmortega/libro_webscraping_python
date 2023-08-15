#!/usr/bin/env python
# -*- coding: utf-8 -*-

import newspaper

cnn_paper = newspaper.build('http://www.cnn.com')

print('category urls:')
for category in cnn_paper.category_urls():
	print(category)
	
print('url articles:')

for article in cnn_paper.articles:
	print(article.url)

