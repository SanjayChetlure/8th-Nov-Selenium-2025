import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.mobikwik.com/")

time.sleep(2)

#click on login btn from main page
driver.find_element(By.XPATH,"(//span[text()='Login'])[1]").click()

#Enter mob num from Hidden division popup
driver.find_element(By.XPATH,"//input[@id='email']").send_keys("9999999999")

time.sleep(5)