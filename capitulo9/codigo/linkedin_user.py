import os
from linkedin_scraper import Person, actions
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome()

email = "email"
password = "password"
user = "user"

actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal
person = Person("https://www.linkedin.com/in/"+user, contacts=[], experiences=[], educations=[], driver=driver)

print("Person: " + person.name)
print("About: " + person.about)

for contact in person.contacts:
	print("Contact: " + contact.name + " - " + contact.occupation + " -> " + contact.url)
	
for experience in person.experiences:
	print("Experience: " + str(experience))
	
for education in person.educations:
	print("Education: " + str(education))
