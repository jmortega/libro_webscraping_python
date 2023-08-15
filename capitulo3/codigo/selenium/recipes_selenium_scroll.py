from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "http://www.yummly.com/recipes?q=&allowedCuisine=cuisine^cuisine-spanish&noUserSettings=true"
driver = webdriver.Chrome()
driver.get(url)

time.sleep(5)

recipes = driver.find_elements(By.CLASS_NAME,"recipe-card")
print ("Recipes number: {}".format(len(recipes)))

# We scroll through javascript code in the browser
driver.execute_script('cookbook = document.getElementsByClassName("cookbook")[0];')
driver.execute_script('maxScroll = document.getElementsByClassName("RecipeGrid")[0].clientHeight;')
driver.execute_script('cookbook.scrollTo(0, maxScroll);')

time.sleep(5)

recipes = driver.find_elements(By.CLASS_NAME,"recipe-card")
print ("Recipes number: {}".format(len(recipes)))

driver.quit()


