#!/usr/bin/env python3

import os
import requests
from bs4 import BeautifulSoup
from scrapy.selector import Selector

class Scraping:    
    def scrapingLinks(self,url):
            print("URL a investigar: "+ url)
        
            try:
                response = requests.get(url)  
                bs = BeautifulSoup(response.text, 'lxml')

                jobtitle = bs.find_all("span", class_= "company-name")
                location = bs.find_all("span", class_=  "listing-location")
                description = bs.find_all("div", class_=  "job-description")
                company = bs.find_all("span", class_= "company-name")
                
                

                jobtitle = Selector(text = str(jobtitle[0])).xpath('//span/text()').get()
                jobtitle = jobtitle.replace("\n", "")
                print(jobtitle.lstrip())

                company = Selector(text = str(company[0])).xpath('//span/text()').getall()
                company = company[3].replace("\n", "")
                company = company.replace("\t", "")
                print(company.lstrip())

                location = Selector(text = str(location[0])).xpath('//a/text()').get()
                print(location)

                description = Selector(text = str(description[0])).xpath('//p/text()').get()
                print(description)

            except Exception as e:
                    print("Error de conexión en:  " + url)
                    pass
					
if __name__ == "__main__":
	target = "https://www.python.org/jobs/7327/"
	scraping = Scraping()
	scraping.scrapingLinks(target)
