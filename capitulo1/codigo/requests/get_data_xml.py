import urllib.request
import xml.etree.ElementTree as ET

url = 'https://www.w3schools.com/xml/cd_catalog.xml'

data = urllib.request.urlopen(url).read()

#utilizamos el método decode() porque los datos están en formato byte
tree = ET.fromstring(data.decode()) 

cd_list = tree.findall('CD')
print('Records number:', len(cd_list))

for item in cd_list:
    print('\r')
    print('Title:', item.find('TITLE').text)
    print('artist:', item.find('ARTIST').text)
    print('price:', item.find('PRICE').text)

