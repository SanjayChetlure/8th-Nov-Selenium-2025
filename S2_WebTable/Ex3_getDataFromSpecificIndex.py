import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("file:///D:/8th%20Nov%20Python%20Automation/Html%20Code/WebTable.html")

time.sleep(2)

value=driver.find_element(By.XPATH,"//table[@id='1234']//tr[4]/td[3]").text
print(value)


time.sleep(5)