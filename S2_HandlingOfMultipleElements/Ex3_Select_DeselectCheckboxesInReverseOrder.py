import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("file:///D:/8th%20Nov%20Python%20Automation/Html%20Code/MultipleCheckboxes.html")
time.sleep(2)

allCheckboxAddress=driver.find_elements(By.XPATH,"//input[@type='checkbox']")

for eachCheckboxAddress in allCheckboxAddress:
    eachCheckboxAddress.click()
    time.sleep(1)

allCheckboxAddress.reverse()

for eachCheckboxAddress in allCheckboxAddress:
    eachCheckboxAddress.click()
    time.sleep(1)


time.sleep(7)