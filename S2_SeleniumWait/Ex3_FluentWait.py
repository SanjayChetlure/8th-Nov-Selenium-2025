import time
from selenium import webdriver
# from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)

wait = WebDriverWait(
   driver,
   timeout=15,             # timeInSec
   poll_frequency=1,       # check every 1 second
   ignored_exceptions=[NoSuchElementException] )

element = wait.until( EC.visibility_of_element_located((By.XPATH, "//button[text()='Log in']")) )
element.click()
time.sleep(5)


