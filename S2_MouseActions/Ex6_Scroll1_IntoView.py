import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.facebook.com/")
time.sleep(2)

instaLink=driver.find_element(By.XPATH,"//a[text()='Instagram']")

act=ActionChains(driver)

act.scroll_to_element(instaLink).perform()



time.sleep(10)