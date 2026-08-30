import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
time.sleep(5)
driver.get("http://watir.com/examples/shadow_dom.html")
time.sleep(5)
driver.find_element(By.XPATH,"//div[@id='shadow_host']").shadow_root.find_element(By.CSS_SELECTOR,"input[type='text']").send_keys("abc")


time.sleep(10)