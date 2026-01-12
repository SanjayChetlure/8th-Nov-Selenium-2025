import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com")

#getText from forgotten pwd link
textValue=driver.find_element(By.XPATH,"//a[contains(text(),'Forgotten ')]").text
print(textValue)

time.sleep(5)