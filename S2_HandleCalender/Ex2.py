from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.makemytrip.com/")
time.sleep(3)

# close login popup (important step)
driver.find_element(By.XPATH, "//span[@class='commonModal__close']").click()
time.sleep(3)

# click on departure field
driver.find_element(By.XPATH, "//label[@for='departure']").click()
time.sleep(3)

target_month = "July 2026"
target_day = "15"

# loop until desired month appears
while True:
    month = driver.find_element(By.XPATH, "(//div[@class='DayPicker-Caption'])[1]").text

    if target_month in month:
        break
    else:
        driver.find_element(By.XPATH, "//span[@aria-label='Next Month']").click()
    time.sleep(1)

# select date
allDates = driver.find_elements(By.XPATH, "//p[@class='dateInnerCell']")
time.sleep(3)

for date in allDates:
    if date.text == target_day:
        date.click()
        break
    time.sleep(1)

time.sleep(10)
driver.quit()