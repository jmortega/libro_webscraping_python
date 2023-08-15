from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup

url = "http://www.yummly.com/recipes?q=&allowedCuisine=cuisine^cuisine-spanish&noUserSettings=true"
driver = webdriver.Chrome()
driver.get(url)

time.sleep(5)

# Nos desplazamos por el código javascript en el navegador
driver.execute_script('cookbook = document.getElementsByClassName("cookbook")[0];')
driver.execute_script('maxScroll = document.getElementsByClassName("RecipeGrid")[0].clientHeight;')
driver.execute_script('cookbook.scrollTo(0, maxScroll);')

time.sleep(5)

recipeContainer = driver.find_element(By.CLASS_NAME,"RecipeContainer")
soup = BeautifulSoup(recipeContainer.get_attribute('outerHTML'), 'lxml')
print(soup)
driver.quit()

#Desde aquí, realizamos el tratamiento con BS4
recipes = soup.find_all('div', {'class': 'recipe-card-img-wrapper'})
print("Recipes number: {}".format(len(recipes)))
for title in recipes:
    print(title.text)

