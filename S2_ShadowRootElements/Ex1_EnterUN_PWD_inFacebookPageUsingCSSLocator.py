import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")

time.sleep(2)
#enter UN
driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc")
time.sleep(2)

#enter PWD
driver.find_element(By.CSS_SELECTOR,"input#pass").send_keys("xyz")


time.sleep(10)
