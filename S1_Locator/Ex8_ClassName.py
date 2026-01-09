import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("file:///D:/8th%20Nov%20Python%20Automation/Html%20Code/ClassName.html")

#enter FN
driver.find_element(By.CLASS_NAME,"xyz123").send_keys("abc")

#enter LN
driver.find_element(By.CLASS_NAME,"xyz123").send_keys("xyz")

time.sleep(10)

