# Importar paquetes
from urllib.request import urlopen, Request

# Indicar la url
url = "http://www.google.com"

# Construimos el objeto Request
request=Request(url)

# Enviar la petición y guardarla en la variable response
response=urlopen(request)

# Imprimir el tipo de la respuesta
print(type(response))

# Extraer el código html de la respuesta
html=response.read()

# Imprimir código html
print(html)

# cerrar la respuesta
response.close()

