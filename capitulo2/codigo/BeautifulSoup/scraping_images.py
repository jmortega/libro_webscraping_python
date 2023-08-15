#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import requests
from lxml import html
from bs4 import BeautifulSoup

class Scraping:
   
				
    def scrapingImages(self,url):
        print("\nScraping the server for images and pdfs.... "+ url)
    
        try:
            response = requests.get(url)  
            parsed_body = html.fromstring(response.text)

            # Grab links to all images
            images = parsed_body.xpath('//img/@src')

            print('Found %s images' % len(images))
    
            #create directory for save images
            os.system("mkdir images")
    
            for image in images:
                if image.startswith("http") == False:
                    download = url + image
                else:
                    download = image
                print(download)
                # download images in images directory
                r = requests.get(download)
                f = open('images/%s' % download.split('/')[-1], 'wb')
                f.write(r.content)
                f.close()
    
        except Exception as e:
                print(e)
                print("Error to connect with " + url + " for scraping the site")
                pass

                
if __name__ == "__main__":
	url = 'http://www.python.org'
	scraping = Scraping()
	scraping.scrapingImages(url)
