import requests
from parsel import Selector

# Realizamos la solicitud al sitio
response = requests.get('https://www.python.org')

# "response.txt" contiene todo el contenido de la página web
selector = Selector(response.text)

# Extracción del atributo href de la etiqueta <a href="*">
href_links = selector.xpath('//a/@href').getall()

# Extracción del atributo src de la etiqueta <img src="*">
image_links = selector.xpath('//img/@src').getall()

#Imprimir enlaces e imágenes
print('href_links:')
print(href_links)

print('image_links:')
print(image_links)

