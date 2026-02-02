import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("file:///D:/8th%20Nov%20Python%20Automation/Html%20Code/WebTable.html")

time.sleep(2)

allCols=driver.find_elements(By.XPATH,"//table[@id='1234']//tr[3]/td")
print(len(allCols))


time.sleep(5)