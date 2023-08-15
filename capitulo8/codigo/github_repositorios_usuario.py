import requests
from bs4 import BeautifulSoup
import re
session = requests.Session()
url = 'https://github.com/{}'

username = input("Introduce nombre usuario:")

response = session.get(url.format(username), params={'page': 1, 'tab':'repositories'})
html_soup = BeautifulSoup(response.text, 'html.parser')

is_normal_user = False
repositorio_element = html_soup.find(class_='repo-list')

if not repositorio_element:
  is_normal_user = True
  repositorio_element = html_soup.find(id='user-repositories-list')

repositorios = repositorio_element.find_all('li')

for repositorio in repositorios:
  name = repositorio.find('a').get_text(strip=True)
  language = repositorio.find(attrs={'itemprop': 'programmingLanguage'})
  language = language.get_text(strip=True) if language else 'unknown' 
  stars = repositorio.find('a', attrs={'href': re.compile('\/stargazers')})
  stars = int(stars.get_text(strip=True).replace(',', '')) if stars else 0
  print('Repositorio:'+ name+ ' Lenguaje:'+ language+' Estrellas:'+ str(stars))
