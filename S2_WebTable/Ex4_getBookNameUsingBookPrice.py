import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("D:\Python\Workspace\8thNov_Selenium\Html Files\WebTable.html")

time.sleep(2)

value=driver.find_element(By.XPATH,"//table[@id='1234']//td[text()='300']//parent::tr/td[2]").text
print(value)
print("hi")


time.sleep(5)


