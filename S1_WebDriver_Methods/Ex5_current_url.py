import time
from selenium import webdriver


driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")

actUrl=driver.current_url
print(actUrl)

print(driver.current_url)