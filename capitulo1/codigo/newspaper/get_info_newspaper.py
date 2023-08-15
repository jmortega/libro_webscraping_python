#!/usr/bin/python3

import newspaper
from newspaper import Article

# hot() devuelve una lista de los principales términos de tendencia en Google usando una API pública
print(newspaper.hot())

# popular_urls() devuelve una lista de URL de fuentes de noticias populares
print(newspaper.popular_urls())
newspaper.languages()

url="http://www.cnn.com"

website = newspaper.build(url)

print(website.brand)

print(website.description)

print("Número de artículos")
print(len(website.articles))

