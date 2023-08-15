import urllib.request
import json

#https://api.openaq.org/v2

url_cities = 'https://api.openaq.org/v2/cities'
country = input('Enter the acronym of the country (for example GB): ')
url_country = url_cities + '?country=' + country
#https://api.openaq.org/v2/cities?country=GB
datos = urllib.request.urlopen(url_country).read().decode()
js = json.loads(datos)
for k in range(50):
    city = js['results'][k]['city']
    print(city)
	
city = input('Enter the name of a city:')
url1 = 'https://api.openaq.org/v2/latest'
url2 = url1 + '?limit=1&city=' + city
#https://api.openaq.org/v2/latest?limit=1&city=Manchester
data = urllib.request.urlopen(url2).read().decode()
js = json.loads(data)
coordinates = js['results'][0]['coordinates']
latitude = coordinates['latitude']
longitude = coordinates['longitude']

print('The coordinates of ', city,  ' are Latitude: ',latitude,' Longitude: ',longitude)

