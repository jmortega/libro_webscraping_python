#!/usr/bin/env python3

import os
import requests
from lxml import html

class Scraping:
   		
    def scrapingImages(self,url):
        print("Obtener imágenes de la url:"+ url)
    
        try:
            response = requests.get(url)  
            parsed_body = html.fromstring(response.text)

            # expresion regular para obtener imagenes
            images = parsed_body.xpath('//img/@src')

            print('Imágenes encontradas %s' % len(images))
    
            #crear directorio para guardar las imagenes
            os.system("mkdir imagenes")
    
            for image in images:
                if image.startswith("http") == False:
                    download = url + "/"+ image
                else:
                    download = image
                print(download)
                # descargar las imagenes en el directorio creado
                r = requests.get(download)
                f = open('imagenes/%s' % download.split('/')[-1], 'wb')
                f.write(r.content)
                f.close()
                
        except Exception as e:
                print("Error de conexión en: " + url)
                pass
                
					
if __name__ == "__main__":
	target = "https://www.python.org"
	scraping = Scraping()
	scraping.scrapingImages(target)
