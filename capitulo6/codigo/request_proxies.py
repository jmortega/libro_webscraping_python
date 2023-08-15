import requests

proxies = {
  'http': 'direccion_ip:puerto',
  'https': 'direccion_ip:puerto',
}

requests.get('http://example.org', proxies=proxies)

