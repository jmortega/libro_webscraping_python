from bs4 import BeautifulSoup
import os, sys
import requests
from fake_useragent import UserAgent

def getAllImages(url):

    ua = UserAgent()
    header = {'user-agent':ua.chrome}
    schedule_page = requests.get(url,headers=header)

    #crear carpeta para guardar las imágenes
    os.system("mkdir images_python")

    bs = BeautifulSoup(schedule_page.text,"html.parser")
    for image in bs.findAll("img"):
        print("found image")
        print(image)

        # Extrae la ubicación de la imagen
        src = image.get('src')
        print(url+src)
        parts_image = src.split("/")
        image_name = parts_image[len(parts_image)-1]

        #Guardar la imagen
        with open("images_python/"+image_name,"wb") as f:
            f.write(requests.get(url+src).content)

getAllImages("http://www.python.org")
