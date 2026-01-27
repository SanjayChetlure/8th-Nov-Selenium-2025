import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.facebook.com/r.php?entry_point=login")
time.sleep(2)

month=driver.find_element(By.XPATH,"//select[@id='month']")

act=ActionChains(driver)

#open listbox options
act.click(month).perform()
time.sleep(2)

#navigate to last option using End key
act.send_keys(Keys.END).perform()
time.sleep(2)

#Navigate to June option using Arrow_UP key
for i in range(6):
    act.send_keys(Keys.ARROW_UP).perform()
    time.sleep(1)

#Select option using Enter key
act.send_keys(Keys.ENTER).perform()

time.sleep(7)