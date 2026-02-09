import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.flipkart.com/")
time.sleep(2)
driver.implicitly_wait(10)

#Enter mob name
driver.find_element(By.XPATH,"//input[@class='lNPl8b']").send_keys("redmi 12 5G")

#click on search btn
driver.find_element(By.XPATH,"//button[@class='kV1UjG']").click()

#get Ratings
ratings=driver.find_element(By.XPATH,"((//div[@class='jIjQ8S'])[1]//span[@class='PvbNMB']//span)[2]").text
print(ratings)

