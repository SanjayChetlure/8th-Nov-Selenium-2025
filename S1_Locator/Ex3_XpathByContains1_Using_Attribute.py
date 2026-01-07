import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")

time.sleep(2)

#enter UN
driver.find_element(By.XPATH,"//input[contains(@placeholder,'Email address')]").send_keys("abc")

#enter pwd
driver.find_element(By.XPATH,"//input[contains(@class,'_6luy _9npi')]").send_keys("xyz")

#click on login btn
driver.find_element(By.XPATH,"//button[contains(@class,'6lth _4jy6 _4jy1')]").click()

time.sleep(10)