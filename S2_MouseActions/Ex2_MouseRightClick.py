import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.flipkart.com/")


cart=driver.find_element(By.XPATH,"//a[text()='Cart']")

act=ActionChains(driver)

#Apr1
# act.move_to_element(cart).perform()
# act.context_click().perform()

#Apr2
# act.move_to_element(cart).context_click().perform()

#Apr3
act.context_click(cart).perform()




time.sleep(10)


