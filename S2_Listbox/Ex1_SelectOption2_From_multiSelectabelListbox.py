import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("file:///D:/8th%20Nov%20Python%20Automation/Html%20Code/Sample3_Listbox.html")


selectCountry=driver.find_element(By.XPATH,"//select[@id='1234']")

s=Select(selectCountry)

s.select_by_visible_text("Ind")
s.select_by_visible_text("Sri")
s.select_by_index(3)


time.sleep(5)