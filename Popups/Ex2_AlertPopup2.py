import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.guru99.com/test/delete_customer.php")

time.sleep(2)

#Enter Customer ID
driver.find_element(By.XPATH,"//input[@name='cusid']").send_keys("12345")

#Click on Submit btn
driver.find_element(By.XPATH,"//input[@name='submit']").click()


#Switch to alert popup
altClassObject=driver.switch_to.alert

#1: getText from Alert Popup
textFromAlertPopup=altClassObject.text
print(textFromAlertPopup)

#2: click on Cancel btn
# altClassObject.dismiss()

#3: click on OK btn from 1st alert popup
altClassObject.accept()

#4: click on OK btn from 2nd alert popup
altClassObject.accept()


#5: Enter value in Alert popup
# altClassObject.send_keys("abc")

time.sleep(10)