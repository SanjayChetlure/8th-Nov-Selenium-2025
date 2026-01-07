import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")

time.sleep(2)

#click on forgotten pwd link
driver.find_element(By.XPATH,"//a[text()='Forgotten password?']").click()


time.sleep(5)