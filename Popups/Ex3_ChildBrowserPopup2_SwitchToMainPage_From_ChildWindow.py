import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.stepcampus.in/playground")
driver.implicitly_wait(10)

#click on Open Selenium Docs in New Tab from main page
driver.find_element(By.XPATH,"//a[text()='Open Selenium Docs in New Tab']").click()
time.sleep(2)

#get child Window ID/Address
allIds=driver.window_handles         #[mainPageId(0), childWindowId(1)]  return address of main page & child window

#switch to child window
driver.switch_to.window(allIds[1])      #String ChildWindowId

#click on about link from Child window
driver.find_element(By.XPATH,"//a[text()='About']").click()
time.sleep(3)

#switch to main window
driver.switch_to.window(allIds[0])
time.sleep(3)

#click on Contact link from main page
driver.find_element(By.XPATH,"//a[text()='Contact']").click()

time.sleep(10)

