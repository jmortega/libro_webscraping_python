from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

startURL="http://www.dominio.com"
browser = webdriver.Chrome()
browser.get(startURL)

# un ejemplo de cómo encontrar el enlace de inicio de sesión y obtener la URL
loginLink = browser.find_element(By.XPATH, "//*[contains(text(), 'Log In')]")
loginURL= loginLink.get_attribute("href")

# cargar cookies de Selenium en requests (para autenticarse a nivel de session)
cookies = browser.get_cookies()
session = requests.Session()
for cookie in cookies:
	session.cookies.set(cookie["name"], cookie["value"])

# enviar la petición POST
auth=("login", "password")
r=session.post(url=loginURL, auth=auth)
# actualiza la página para ver el resultado
browser.refresh() 

