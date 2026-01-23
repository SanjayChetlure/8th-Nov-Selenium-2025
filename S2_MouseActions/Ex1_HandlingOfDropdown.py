import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.flipkart.com/")

#step1:identify dropdown element
login=driver.find_element(By.XPATH,"//span[text()='Login']")

#Step2: Create an object of ActionChain class with webdriver obj an inp
act=ActionChains(driver)

#step3
act.move_to_element(login).perform()
time.sleep(2)

#click on orders link from dropdown
driver.find_element(By.XPATH,"//li[text()='Orders']").click()

time.sleep(10)


