import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.instagram.com/")

time.sleep(2)

result=driver.find_element(By.XPATH,"//button[@class=' _aswp _aswr _aswu _asw_ _asx2']").is_enabled()
print(result)

if result:
    print("Element is Enabled")
else:
    print("Element is disabled")

time.sleep(5)