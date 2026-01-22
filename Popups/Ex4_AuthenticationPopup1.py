import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()

# Syntax:   https://username:password@remaingURL
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

time.sleep(10)

