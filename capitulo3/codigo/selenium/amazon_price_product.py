from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.headless = True
driver = webdriver.Chrome(chrome_options=options)

url = 'https://www.amazon.com/Art-Invisibility-Worlds-Teaches-Brother/dp/0316380520/'
driver.get(url)
price = driver.find_element(By.CLASS_NAME,'a-price')
print(price.text)
