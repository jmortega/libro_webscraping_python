#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

url = 'https://www.python.org'
file_name = 'python.org.txt'

page = requests.get(url)
print(page.content)
with open(file_name,'w') as file:
    file.write(page.content.decode('utf-8')) 
