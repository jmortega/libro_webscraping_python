from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://www.google.com")
print(browser.get_cookies())

# session cookies
for cookie in browser.get_cookies():  
    # handle
    print(cookie)


