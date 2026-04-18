from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/date-picker")

driver.maximize_window()
time.sleep(3)

# click on date field
driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']").click()
time.sleep(3)

# select year
yr= driver.find_element(By.XPATH,"//select[@class='react-datepicker__year-select']")
s = Select(yr)
s.select_by_visible_text("2007")

# select month
month = driver.find_element(By.XPATH,"//select[@class='react-datepicker__month-select']")
s = Select(month)
s.select_by_visible_text("July")
time.sleep(3)

# select date
day=8
driver.find_element(By.XPATH, f"(//div[text()='{day}'])[1]").click()

time.sleep(10)
driver.quit()