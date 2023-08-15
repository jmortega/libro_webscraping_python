from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('http://www.python.org')
driver.get_screenshot_as_file('python.png')
driver.close()
