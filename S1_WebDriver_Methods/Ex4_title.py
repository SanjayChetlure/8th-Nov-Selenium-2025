import time
from selenium import webdriver


driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")

actTitle=driver.title
print(actTitle)

print(driver.title)