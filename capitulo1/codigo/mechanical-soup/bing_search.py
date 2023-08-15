#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mechanicalsoup

# Conectando con el motor de búsqueda bing
browser = mechanicalsoup.StatefulBrowser()
browser.open("http://www.bing.com")

# Rellenar el campo de búsqueda
browser.select_form('#sb_form')
browser["q"] = "MechanicalSoup"
browser.submit_selected()

# Obtener resultados en forma de enlaces
for link in browser.links():
    print(link.text, '->', link.attrs['href'])

