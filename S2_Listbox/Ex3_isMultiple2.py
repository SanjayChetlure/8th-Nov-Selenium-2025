import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/r.php?entry_point=login")


month=driver.find_element(By.XPATH,"//select[@id='month']")

s=Select(month)

result=s.is_multiple
print(result)

