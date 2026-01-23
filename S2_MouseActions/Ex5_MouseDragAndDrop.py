import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.guru99.com/test/drag_drop.html")
time.sleep(2)


src=driver.find_element(By.XPATH,"(//a[@class='button button-orange'])[2]")
dest=driver.find_element(By.XPATH,"(//div[@class='ui-widget-content'])[3]")

act=ActionChains(driver)

# act.drag_and_drop(src,dest).perform()

act.move_to_element(src).click_and_hold().move_to_element(dest).release().perform()



time.sleep(10)


