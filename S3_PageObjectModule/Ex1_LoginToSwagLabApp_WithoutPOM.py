import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Edge()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
driver.implicitly_wait(5)

#Enter UN
driver.find_element(By.XPATH,"//input[@name='user-name']").send_keys("standard_user")

#Enter PWD
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("secret_sauce")

time.sleep(2)
#click on login btn
driver.find_element(By.XPATH,"//input[@name='login-button']").click()
time.sleep(2)

#get actual header
actHeader=driver.find_element(By.XPATH,"//div[@class='app_logo']").text
expHeader="Swag Labs1"

if actHeader==expHeader:
    print("TC Pass")
else:
    print("TC Fail")


time.sleep(5)
