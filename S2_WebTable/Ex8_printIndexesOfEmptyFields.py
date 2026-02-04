import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("file:///D:/8th%20Nov%20Python%20Automation/Html%20Code/WebTable.html")

time.sleep(2)

emptyCol = 0
allRows=driver.find_elements(By.XPATH,"//table[@id='1234']//tr")


rowIndex=1
for singleRow in allRows:
    allCols = singleRow.find_elements(By.TAG_NAME, "td")
    colIndex=1
    for singleCol in allCols:
        if singleCol.text=="":
            print("row index: ",rowIndex," col index: ",colIndex)
        colIndex+=1
    print()
    rowIndex+=1

