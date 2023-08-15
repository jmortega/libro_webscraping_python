# Importar el paquete
import requests

# Indicar la url
url = "http://www.google.com"

#  Enviar la petición y guardarla en la variable response
response = requests.get(url)

#  Imprimir el tipo de la respuesta
print(type(response))

# Extraer el código html de la respuesta
html = response.text

# Imprimir código html
print(html)

