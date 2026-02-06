import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)

#Wait for element to be clickable
wait = WebDriverWait(driver, 5)
element = wait.until( EC.visibility_of_element_located((By.XPATH, "//button[text()='Log in']")) )
element.click()

time.sleep(10)






