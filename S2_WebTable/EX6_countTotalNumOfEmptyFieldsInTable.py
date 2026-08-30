import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("file:///D:/Python/Workspace/8thNov_Selenium/Html%20Files/WebTable.html")

time.sleep(2)


allCols = driver.find_elements(By.XPATH, "//table[@id='1234']//td")

emptyCol = 0

for singleCol in allCols:
    text=singleCol.text.strip()
    if text == "":
        emptyCol += 1

print("Total empty fields:", emptyCol)