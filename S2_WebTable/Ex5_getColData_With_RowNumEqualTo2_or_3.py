import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("file:///D:/8th%20Nov%20Python%20Automation/Html%20Code/WebTable.html")

time.sleep(2)


col2_Data=driver.find_elements(By.XPATH,"//table[@id='1234']//tr[position()=3 or position()=4]/td[2]")
print("--Total Elements:-- ",len(col2_Data))

#get data from col2 with rowNum=3 and rowNum=4
for i in col2_Data:
    print(i.text)

time.sleep(5)