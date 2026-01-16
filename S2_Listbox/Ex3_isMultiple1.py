import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("file:///D:/8th%20Nov%20Python%20Automation/Html%20Code/Sample3_Listbox.html")

selectCountry=driver.find_element(By.XPATH,"//select[@id='1234']")

s=Select(selectCountry)

result=s.is_multiple
print(result)

if result:
    print("Listbox is Multi-Selectable")
else:
    print("Listbox is Single-Selectable")


time.sleep(5)

