from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://stackoverflow.com/tags")
page = driver.page_source
print(page)
tags = driver.find_elements(By.CLASS_NAME,"post-tag")
for i in range(len(tags)):
	print(tags[i].text)
