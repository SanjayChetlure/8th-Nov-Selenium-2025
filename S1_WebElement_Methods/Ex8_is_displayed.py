import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.get("https://www.facebook.com")

time.sleep(2)

result=False

try:
    result = driver.find_element(By.XPATH, "//img[@class='fb_logo _8ilh img']").is_displayed()
except:
    print("Exception handled")

print(result)

if result:
    print("Logo Present")
else:
    print("Logo Not Present")



