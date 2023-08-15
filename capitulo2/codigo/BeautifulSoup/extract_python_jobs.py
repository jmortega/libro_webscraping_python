from bs4 import BeautifulSoup
import requests

def getPythonJobs(url):
  # We make the request to the page
  req = requests.get(url)
  # We verify that the request returns a Status Code = 200 (200 = Ok)
  statusCode = req.status_code
  if statusCode == 200:
    # We pass the HTML content of the web to a BeautifulSoup object
    html = BeautifulSoup(req.text, "html.parser")
    # We get all the span elements with class "listing-company-name"
    elements = html.find_all('span', {'class': 'listing-company-name'})
    print(elements)
    # We go through all the entries to extract the text
    for item in elements:
      title = item.find('a')
      # Print text
      print("Job: " + title.text)
      print("**********************************")
  else:
    # If the page does not exist we show the error
    print("The url " + url + " gives an error %d" % statusCode)

getPythonJobs("https://www.python.org/jobs")
