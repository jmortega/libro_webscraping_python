#!/usr/bin/env python3

import os
import requests
from lxml import html

class Scraping:
                
    def scrapingLinks(self,url):
            print("Obtener links de la url:"+ url)
        
            try:
                response = requests.get(url)  
                parsed_body = html.fromstring(response.text)
    
                # expresion regular para obtener links
                links = parsed_body.xpath('//a/@href')
    
                print('Links encontrados %s' % len(links))
    
                for link in links:
                    if(link.startswith("http")):
                        print(link)
                    else:
                        print(url+link)
                    
            except Exception as e:
                    print("Error de conexión en:  " + url)
                    pass
					
if __name__ == "__main__":
	target = "https://www.python.org"
	scraping = Scraping()
	scraping.scrapingLinks(target)
