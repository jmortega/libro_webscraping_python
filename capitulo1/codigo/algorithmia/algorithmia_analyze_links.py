import Algorithmia

input = ["http://python.org",1]

API_KEY ='simU+xQFB6Ts4O306dxEhZreKBA1'

client = Algorithmia.client(API_KEY)
response = client.algo('web/SiteMap/0.1.7').pipe(input)
siteMap = response.result

links = []
output = []

for keyLink in siteMap:
    links.append(keyLink)
    for valLink in siteMap[keyLink]:
        links.append(valLink)

links = list(set(links))
print(links)

for link in links:
    analyze = client.algo('web/AnalyzeURL/0.2.17').pipe(link)
    output.append(analyze.result)

print(json.dumps(output, indent=4))

