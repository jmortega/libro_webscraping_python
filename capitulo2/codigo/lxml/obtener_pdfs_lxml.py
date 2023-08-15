#!/usr/bin/env python3

import os
import requests
from lxml import html

class Scraping:
   		
    def scrapingPDFs(self,url):
        print("Obtener pdfs de la url:"+ url)
    
        try:
            response = requests.get(url)  
            parsed_body = html.fromstring(response.text)

            # expresion regular para obtener pdf
            pdfs = parsed_body.xpath('//a[@href[contains(., ".pdf")]]/@href')

            print('Pdfs encontrados %s' % len(pdfs))
    
            #crear directorio para guardar los documentos
            os.system("mkdir pdfs")
    
            for pdf in pdfs:
                if pdf.startswith("http") == False:
                    download = url + "/"+ pdf
                else:
                    download = pdf
                print(download)
                # download document en el directorio creado
                r = requests.get(download)
                f = open('pdfs/%s' % download.split('/')[-1], 'wb')
                f.write(r.content)
                f.close()
                
        except Exception as e:
                print("Error de conexión en: " + url)
                pass
					
if __name__ == "__main__":
	target = "https://docs.python-guide.org"
	scraping = Scraping()
	scraping.scrapingPDFs(target)
