import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/browser-windows")
driver.implicitly_wait(10)

#click on New Tab from main page
driver.find_element(By.XPATH,"//button[text()='New Tab']").click()
time.sleep(2)

#get child Window ID/Address
allIds=driver.window_handles         #[mainPageId(0), childWindowId(1)]  return address of main page & child window

#switch to child window
driver.switch_to.window(allIds[1])      #String ChildWindowId

#click on about link from Child window
print(driver.title)

#switch to main window
driver.switch_to.window(allIds[0])
time.sleep(3)

#click on NewWindow link from main page
driver.find_element(By.XPATH,"//button[text()='New Window']").click()

#get child Window ID/Address
allIds2=driver.window_handles

# Switch to child window 2
driver.switch_to.window(allIds2[2])
time.sleep(3)

driver.maximize_window()


time.sleep(10)

