from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://websistent.com/tools/htdigest-generator-tool/"
user = "myUser"

driver = webdriver.Chrome()
driver.get(url)

element = driver.find_element(By.ID,"uname")
element.send_keys(user)

#Si vamos al navegador veremos que hemos completado la primera entrada del formulario.
#Luego completamos el resto de entradas

element = driver.find_element(By.ID,"realm")
element.send_keys("myRealm")

element = driver.find_element(By.ID,"word1")
element.send_keys("mypassword")

element = driver.find_element(By.ID,"word2")
element.send_keys("mypassword")

#Finalmente, buscamos el botón y hacemos click
driver.find_element(By.ID,"generate").click();

# Esperamos 2 segundos antes de buscar el elemento
time.sleep(2)

try:
    #Esperamos un máximo de 10 segundos mientras esperamos que desaparezca el texto "Cargando"
    WebDriverWait(driver, 10).until_not(lambda driver: driver.find_element(By.ID,"output").text.startswith("Loading"))

    output = driver.find_element(By.ID,"output").text
    print (output[output.find(user):])

except TimeoutException:
    print("The realm could not be generated or the page has taken too long time to load")
	
finally:
    driver.quit()
