import os
import requests
from lxml import html
from bs4 import BeautifulSoup

class Scraping:

	def scrapingPdfs(self,url):
	
		print("\nScraping the server for images and pdfs.... "+ url)
		try:
			response = requests.get(url)
			parsed_body = html.fromstring(response.text)
			# Grab links to all pdf
			pdfs = parsed_body.xpath('//a[@href[contains(., ".pdf")]]/@href')
			#create directory for save pdfs
			if len(pdfs) >0:
				os.system("mkdir pdfs")
			print('Found %s pdf' % len(pdfs))
			for pdf in pdfs:
				if pdf.startswith("http") == False:
					download = url + pdf
				else:
					download = pdf
				print(download)
				# download pdfs in pdf directory
				r = requests.get(download)
				f = open('pdfs/%s' % download.split('/')[-1], 'wb')
				f.write(r.content)
				f.close()
		
		except Exception as e:
			print(e)
			print("Error to connect with " + url + " for scraping the site")
			pass
              
           
if __name__ == "__main__":
	url = 'https://docs.python-guide.org'
	scraping = Scraping()
	scraping.scrapingPdfs(url)
