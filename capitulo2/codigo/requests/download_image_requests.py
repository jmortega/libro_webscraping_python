from lxml import html, etree
import requests
# Obtenemos el contenido html original de la página web
webpageLink = 'http://www.python.org'
page = requests.get(webpageLink)
# convertir los datos recibidos en HTML de búsqueda
extractedHtml = html.fromstring(page.content)
# consulta XPath para encontrar el enlace de la imagen
# el atributo 'src' de la etiqueta 'img'
imageSrc = extractedHtml.xpath("//img/@src")
print(imageSrc)
# sólo nos interesa la url base
imageDomain = webpageLink.rsplit('http://', 1)
print(imageDomain)
# comprobar si es un enlace absoluto o relativo
if imageSrc[0].startswith("http"):
    # si comienza con http, se trata de un enlace absoluto
    imageLink = imageSrc[0]
else:
	# si no comienza con http, se trata de un enlace relativo
	imageLink = "http://" + str(imageDomain[1]) + str(imageSrc[0])
    
# extraer nombre fichero del enlace
filename = imageLink.split("/")[-1] 
print(imageLink)
# descarga la imagen mediante una petición GET
rawImage = requests.get(imageLink, stream=True)
# guardar la imagen como un fichero
with open(filename, 'wb') as fd:
    for chunk in rawImage.iter_content(chunk_size=1024):
        fd.write(chunk)



