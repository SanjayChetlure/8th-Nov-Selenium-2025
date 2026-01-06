import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")

# driver.find_element("Locator type")
# driver.find_element(By.XPATH,"Xpath Xpression")
#Enter UN
driver.find_element(By.XPATH,"//input[@name='email']").send_keys("abc123")

#Enter PWD
driver.find_element(By.XPATH,"//input[@id='pass']").send_keys("abc@1234")

#click on login btn
driver.find_element(By.XPATH,"//button[@name='login']").click()


time.sleep(10)