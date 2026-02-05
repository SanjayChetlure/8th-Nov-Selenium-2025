import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://books-pwakit.appspot.com/explore?q=")

time.sleep(2)


driver.find_element(By.XPATH,"//book-app[@apptitle='BOOKS']").shadow_root.find_element(By.CSS_SELECTOR,"input#input").send_keys("abc")


time.sleep(10)