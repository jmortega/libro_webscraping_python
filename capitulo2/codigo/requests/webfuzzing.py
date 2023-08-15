#!/usr/bin/python

import requests

user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36'

host='http://testphp.vulnweb.com/'
filepath = 'wordlist_fuzzing.txt'

with open(filepath) as fp:
    line = fp.readline()
    while line:
        url = host+line.strip()
        response = requests.get(url, headers={'User-Agent': user_agent})
        if response.status_code == 200:
            print(url)
        line = fp.readline()
