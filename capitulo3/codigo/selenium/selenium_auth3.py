from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

url = "http://www.dominio.com/"
user = "user"
password = "password"

driver = webdriver.Chrome()
driver.get(url)

WebDriverWait(driver, 10).until(EC.alert_is_present())
alert = driver.switch_to.alert
alert.send_keys(user + Keys.TAB + password )
alert.accept()

