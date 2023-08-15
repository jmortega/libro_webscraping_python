#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

url = "http://www.yummly.com/recipes?q=&allowedCuisine=cuisine^cuisine-spanish&noUserSettings=true"

response = requests.get(url)

# We verify that the request returns a Status Code = 200
statusCode = response.status_code
if statusCode == 200:

    # We pass the HTML content of the web to a BeautifulSoup () object
    html = BeautifulSoup(response.text, "lxml")
    recipes = html.select(".recipe-card")
    print ("Recipes number: {}".format(len(recipes)))
    
else:
    print (statusCode)

