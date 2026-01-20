import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_myfirst")

#switch to frame
driver.switch_to.frame("iframeResult")      #String frameId/frameName

#click on date & time btn
driver.find_element(By.XPATH,"//button[contains(text(),'Click me')]").click()
time.sleep(5)

#Switch to main page
# driver.switch_to.parent_frame()
driver.switch_to.default_content()

#click on menu option from main page
driver.find_element(By.XPATH,"//a[@id='menuButton']").click()

time.sleep(10)
