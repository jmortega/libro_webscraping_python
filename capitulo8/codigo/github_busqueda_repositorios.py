import requests

busqueda  = input("Cadena de busqueda:")

response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': busqueda},
)

json_response = response.json()
repositorios = json_response['items']
for repositorio in repositorios:
	print(f'URL: {repositorio["url"]}')
	print(f'Nombre: {repositorio["name"]}')
	print(f'Descripcion: {repositorio["description"]}')
	print(f'Topics: {repositorio["topics"]}')
