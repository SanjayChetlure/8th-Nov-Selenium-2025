import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_myfirst")

#switch to frame
#apr1:
# frameAddress=driver.find_element(By.XPATH,"//iframe[@id='iframeResult']")
# driver.switch_to.frame(frameAddress)       #Frame WebElement

#apr2:
driver.switch_to.frame("iframeResult")      #String frameId/frameName

#apr3:
# driver.switch_to.frame()      #int frameIndex


#click on date & time btn
driver.find_element(By.XPATH,"//button[contains(text(),'Click me')]").click()

time.sleep(10)
