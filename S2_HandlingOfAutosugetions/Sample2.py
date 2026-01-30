import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com")
time.sleep(2)

#enter mobile name
driver.find_element(By.XPATH,"//textarea[@class='gLFyf']").send_keys("redmi")
time.sleep(2)

expText="redmi note 15 pro plus"

allOptionsAddress=driver.find_elements(By.XPATH,"(//ul[@class='G43f7e'])[1]/li//div[@class='wM6W7d']")


for i in allOptionsAddress:
    actText=i.text                 #redmi note 14
    if actText==expText:           #redmi note 14==redmi note 14
        i.click()
        break

time.sleep(20)