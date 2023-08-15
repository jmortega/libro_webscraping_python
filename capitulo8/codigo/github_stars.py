import requests
from bs4 import BeautifulSoup
import re
session = requests.Session()
url = 'https://github.com/{}'
username = 'google'
r = session.get(url.format(username), params={'page': 1, 'tab':'repositories'})
html_soup = BeautifulSoup(r.text, 'html.parser')
repos_element = html_soup.find(class_='repo-list')
if not repos_element:
	usuario_normal = True
	repos_element = html_soup.find(id='user-repositories-list')

repositorios = repos_element.find_all('li')

for repositorio in repositorios:
	if repositorio is not None: 
		nombre = repositorio.find('a').get_text(strip=True)
		lenguaje = repositorio.find(attrs={'itemprop': 'programmingLanguage'})
		lenguaje = lenguaje.get_text(strip=True) if lenguaje else 'desconocido'
		estrellas = repositorio.find('a', attrs={'href': re.compile('\/stargazers')})
		estrellas = int(estrellas.get_text(strip=True).replace(',', '')) if estrellas else 0 
		print(nombre, lenguaje, estrellas)

