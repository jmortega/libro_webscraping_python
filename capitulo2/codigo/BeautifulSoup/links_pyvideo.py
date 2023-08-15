#!/usr/bin/env python3

import urllib.request
from bs4 import BeautifulSoup

def get_video_links(archive_url):
    # crear objeto respuesta
    response = urllib.request.urlopen(archive_url)
    # crear objeto beautiful-soup
    soup = BeautifulSoup(response.read(),'lxml')
    links = []
    for link in soup.find_all('a'):
        file_link = link.get('href')
        links.append(file_link)
    return links

links = get_video_links('https://pyvideo.org')
print(links)
