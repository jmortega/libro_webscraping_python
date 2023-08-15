from selenium import webdriver

user = "usuario"
password = "password"

driver = webdriver.Chrome()
driver.get("http://{}:{}@www.dominio.com".format(user,  password))

