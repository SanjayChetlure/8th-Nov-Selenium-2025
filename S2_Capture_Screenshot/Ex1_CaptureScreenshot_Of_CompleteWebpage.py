import time
from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://www.google.com")

driver.save_screenshot("D:\\8th Nov Python Automation\\Screenshots\\abc2.jpg")


time.sleep(5)