import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/r.php?entry_point=login")


#click on female radio btn
driver.find_element(By.XPATH,"(//input[@class='_8esa'])[1]").click()


time.sleep(5)