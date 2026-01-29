import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.facebook.com")
time.sleep(2)

allLinksAddress=driver.find_elements(By.XPATH,"//a")
print(len(allLinksAddress))

for i in allLinksAddress:
    value=i.text
    print(value)


time.sleep(7)