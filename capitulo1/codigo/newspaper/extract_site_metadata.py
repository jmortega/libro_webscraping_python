#!/usr/bin/env python
# -*- coding: utf-8 -*-

import extruct
import requests
import pprint
from w3lib.html import get_base_url

pp = pprint.PrettyPrinter(indent=4)
r = requests.get('https://www.python.org')
base_url = get_base_url(r.text, r.url)
data = extruct.extract(r.text, base_url=base_url)
pp.pprint(data)
