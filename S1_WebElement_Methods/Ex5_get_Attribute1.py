import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com")

value=driver.find_element(By.XPATH,"//input[@name='email']").get_attribute("placeholder")
print(value)