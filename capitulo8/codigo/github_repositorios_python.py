import json
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup

def scrap_website(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    is_normal_user = False
    repositorio_element = soup.find(class_='repo-list')
    
    if not repositorio_element:
    	is_normal_user = True
    	repositorio_element = html_soup.find(id='user-repositories-list')
    	
    lista_repositorios = repositorio_element.find_all('li')
    results = []

    for repo in lista_repositorios:
        repository = {}
        repository["name"] = repo.a.string.strip()
        base_url = '{uri.scheme}://{uri.netloc}'.format(uri=urlparse(url))
        repository["link"] = "{0}{1}".format(base_url, repo.a.get('href'))
        if repo.p and repo.p.string:
            repository["description"] = repo.p.string.strip()
        else:
            repository["description"] = "No description available for this repository."
        programming_language = soup.find(attrs={"itemprop": "programmingLanguage"}).string.strip()
        repository["programming_language"] = programming_language
        results.append(repository)

    return results

print(json.dumps(scrap_website("https://github.com/python?tab=repositories"), indent=4))
