import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.flipkart.com/")
time.sleep(2)


cart=driver.find_element(By.XPATH,"//a[text()='Cart']")

act=ActionChains(driver)

#Apr1
# act.move_to_element(cart).perform()
# act.click().perform()

#Apr2
# act.move_to_element(cart).click().perform()

#Apr3
act.click(cart).perform()




time.sleep(10)


