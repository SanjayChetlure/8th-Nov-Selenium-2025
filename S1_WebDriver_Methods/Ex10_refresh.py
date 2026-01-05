import time
from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(4)
driver.refresh()


time.sleep(10)