import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("file:///D:/8th%20Nov%20Python%20Automation/Html%20Code/LinkText_PartialLinkText.html")

time.sleep(3)
#click on facebook link
driver.find_element(By.PARTIAL_LINK_TEXT,"face").click()

time.sleep(10)

