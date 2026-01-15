import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com")

# driver.find_element(By.XPATH,"//img[@class='fb_logo _8ilh img']").screenshot("D:\\8th Nov Python Automation\\Screenshots\\logo.png")


logo=driver.find_element(By.XPATH,"//img[@class='fb_logo _8ilh img']")
logo.screenshot("D:\\8th Nov Python Automation\\Screenshots\\logo2.png")

time.sleep(5)