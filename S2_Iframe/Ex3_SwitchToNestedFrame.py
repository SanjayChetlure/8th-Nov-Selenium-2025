import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://autotestsandbox.com/examples/nested-iframes")

#switch to outer frame
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@title='Outer nested frame']"))

#switch to Inner frame
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@title='Inner']"))

#get text from nested frame
value=driver.find_element(By.XPATH,"//p[text()='Inner iframe content']").text
print(value)

time.sleep(10)
