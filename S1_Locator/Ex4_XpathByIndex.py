import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/r.php?entry_point=login")

#enter FN
driver.find_element(By.XPATH,"(//input[@type='text'])[1]").send_keys("abc")

#enter LN
driver.find_element(By.XPATH,"(//input[@type='text'])[2]").send_keys("xyz")

#enter mob num
driver.find_element(By.XPATH,"(//input[@type='text'])[5]").send_keys("1111")

time.sleep(10)