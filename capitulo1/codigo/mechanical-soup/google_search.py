#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mechanicalsoup

browser = mechanicalsoup.StatefulBrowser()
browser.open("https://www.google.com")

browser.select_form('form[action="/search"]')
browser["q"] = "MechanicalSoup"

browser.submit_selected(btnName="btnG")
print(browser.get_current_page())

for link in browser.links():
    print(link.text, '->', link.attrs['href'])
