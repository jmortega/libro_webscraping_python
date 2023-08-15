from bs4 import BeautifulSoup
import requests
import csv

url = "http://python.org"

csv_file = csv.writer(open("data_links.csv", "w"))
csv_file.writerow(["Section" , "Link"])

# Obtener la página web y crear un objeto de respuesta.
response = requests.get(url)

# Extrayendo el código fuente de la página
data = response.text

# crear un objeto BeautifulSoup
soup = BeautifulSoup(data, 'html.parser')

# Usamos la función 'find_all' para recuperar todas las instancias de la etiqueta 'a' en el HTML # y almacenamos en la variable 'tags'
# Extraer todas las etiquetas <a> en una lista
tags = soup.find_all('a')

# Extracción de URL del atributo href en las etiquetas <a>.
for tag in tags:
	print(tag.get('href'))
	link = tag.get('href')
	text = tag.get_text()
	csv_file.writerow([text, link])

