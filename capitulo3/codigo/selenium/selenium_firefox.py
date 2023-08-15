from selenium import webdriver
from selenium.webdriver.firefox.options import Options

'''La opcion headless lo que hace que no se abra el navegador, si no que se ejecute en segundo plano'''
options = Options()
options.add_argument('-headless')

try:
    driver = webdriver.Firefox(options=options)
    print ("Headless Firefox Initialized")
    driver.get('http://python.org')
    driver.quit()
except Exception as exception:
    print(exception)

