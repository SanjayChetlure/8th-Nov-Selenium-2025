import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")

#apr1
# driver.find_element(By.XPATH,"//input[@name='email']").send_keys("abc")
# time.sleep(2)
# driver.find_element(By.XPATH,"//input[@name='email']").clear()
# time.sleep(2)
# driver.find_element(By.XPATH,"//input[@name='email']").send_keys("xyz")

#apr2
UN=driver.find_element(By.XPATH,"//input[@name='email']")
UN.send_keys("abc")
time.sleep(2)
UN.clear()
time.sleep(2)
UN.send_keys("xyz")


time.sleep(5)