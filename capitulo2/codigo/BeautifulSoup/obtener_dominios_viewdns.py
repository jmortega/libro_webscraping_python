import requests
from bs4 import BeautifulSoup

#https://viewdns.info/reverseip/?host=bing.com&t=1
#El servicio permite obtener otros dominios alojados en el mismo servidor donde se aloja el dominio que estamos analizando

def main():
    sitio = "bing.com"
    agent = {'User-Agent':'Firefox'}
    response = requests.get("https://viewdns.info/reverseip/?host={}&t=1".format(sitio),headers=agent)
    html = BeautifulSoup(response.text,'html.parser')
    tabla = html.find_all('table',attrs={'border':'1'})[0]
    #Para cada una de las filas
    for fila in tabla.find_all("tr"):
        print("Dominio alojado en el mismo servidor: " + fila.td.string)

if __name__ == '__main__':
    main()

