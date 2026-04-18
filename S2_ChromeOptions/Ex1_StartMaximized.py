import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

ops = Options()
ops.add_argument("--start-maximized")

driver = webdriver.Chrome(options=ops)
driver.get("https://www.google.com/")

time.sleep(5)