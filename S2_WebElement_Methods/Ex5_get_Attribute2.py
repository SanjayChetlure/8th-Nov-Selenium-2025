import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com")

#enter UN
driver.find_element(By.XPATH,"//input[@name='email']").send_keys("abc@gmail.com")
time.sleep(3)

inpText=driver.find_element(By.XPATH,"//input[@name='email']").get_attribute("value")
print(inpText)


time.sleep(10)