import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("file:///D:/8th%20Nov%20Python%20Automation/Html%20Code/WebTable.html")

time.sleep(2)

driver.find_element(By.XPATH).find_elements()


allRowsAddress=driver.find_elements(By.XPATH,"//table[@id='1234']//tr")   #[row1Address, row2Address, row3Address, row4Address]

for singleRowAddress in allRowsAddress:                     #rows-> create outer for loop
    allColsAddress = singleRowAddress.find_elements(By.TAG_NAME, "td")          #[col1Address, col2Address, col3Address]
    for singleColAdress in allColsAddress:                  #cols -> create inner for loop
        print(singleColAdress.text, end=" ")                #print data in inner for loop without line break
    print()                                                 #call empty print() after inner for loop



#1  Selenium 100
