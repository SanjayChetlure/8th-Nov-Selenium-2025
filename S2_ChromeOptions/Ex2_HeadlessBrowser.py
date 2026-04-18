import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

ops = Options()
ops.add_argument("--headless")

driver = webdriver.Chrome(options=ops)
driver.get("https://www.google.com/")
print(driver.title)

time.sleep(5)