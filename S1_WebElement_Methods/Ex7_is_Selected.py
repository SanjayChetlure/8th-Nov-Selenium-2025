import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/r.php?entry_point=login")

time.sleep(2)

result=driver.find_element(By.XPATH,"(//input[@class='_8esa'])[1]").is_selected()
print(result)

if result:
    print("radio btn is selected")
else:
    print("radio btn is de-selected")

time.sleep(5)