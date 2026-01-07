import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")

time.sleep(2)

#click on login btn
driver.find_element(By.XPATH,"//button[contains(text(),'in')]").click()


time.sleep(5)