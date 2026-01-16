import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/r.php?entry_point=login")

#Step1:
month=driver.find_element(By.XPATH,"//select[@id='month']")

#Step2:
s=Select(month)

#Step3:
# s.select_by_visible_text("Nov")      #String text
# s.select_by_value("7")       #String value
s.select_by_index(3)

time.sleep(5)