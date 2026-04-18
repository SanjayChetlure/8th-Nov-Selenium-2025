import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--force-device-scale-factor=1")

driver = webdriver.Chrome(options=options)
driver.get("https://google.com/")
driver.maximize_window()
time.sleep(5)