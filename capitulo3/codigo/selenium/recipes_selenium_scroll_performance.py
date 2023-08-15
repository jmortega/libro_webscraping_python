#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time

def heightHasChanged(driver, lastHeight):
    """
    Comprueba si, tras hacer scroll, el tamaño del panel en el que están las recetas ha cambiado
    """
    new_height = driver.execute_script('return document.getElementsByClassName("RecipeGrid")[0].clientHeight;')
    return last_height!= new_height

url = "http://www.yummly.com/recipes?q=&allowedCuisine=cuisine^cuisine-spanish&noUserSettings=true"
driver = webdriver.Chrome()
driver.get(url)

last_height = 0

time.sleep(10)

try:
    while True:
        # Nos desplazamos por el código javascript en el navegador
        driver.execute_script('cookbook = document.getElementsByClassName("cookbook")[0];')
        driver.execute_script('maxScroll = document.getElementsByClassName("RecipeGrid")[0].clientHeight;')
        driver.execute_script('cookbook.scrollTo(0, maxScroll);')

        # Esperamos hasta que se actualice el desplazamiento o lleguemos al final
        WebDriverWait(driver, 15).until(lambda driver: heightHasChanged(driver,last_height))
        
        last_height = driver.execute_script('return document.getElementsByClassName("RecipeGrid")[0].clientHeight;')

except TimeoutException:
    # En este punto, podemos suponer que nos hemos desplazado hasta el final
    recipes = driver.find_elements(By.CLASS_NAME,"recipe-card")
    print ("Recipes number: {}".format(len(recipes)))

finally:
    driver.quit()

