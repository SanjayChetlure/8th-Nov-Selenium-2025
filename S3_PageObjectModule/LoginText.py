import time
from selenium import webdriver
from S3_PageObjectModule.HomePage import SwagLabHomePage
from S3_PageObjectModule.LoginPage import SwagLabLoginPage

def TC1_swagLabLogin():
    driver=webdriver.Edge()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.implicitly_wait(5)

    login=SwagLabLoginPage(driver)
    login.enterUsername("standard_user")
    time.sleep(1)
    login.enterPassword("secret_sauce")
    time.sleep(1)
    login.clickOnLoginBtn()

    home=SwagLabHomePage(driver)
    actHederName=home.getHeaderName()
    expHeaderName="Swag Labs"

    if actHederName==expHeaderName:
        print("TC Pass")
    else:
        print("TC Fail")

# TC1_swagLabLogin()



def TC2_loginToSwagLabWithInvalidCredentials():
    driver = webdriver.Edge()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.implicitly_wait(5)

    login = SwagLabLoginPage(driver)
    login.enterUsername("standard_user")
    time.sleep(1)
    login.enterPassword("abcd")
    time.sleep(1)
    login.clickOnLoginBtn()
    time.sleep(2)
    actErrorMsg=login.getLoginFailedErrorMsg()
    expErrorMsg="Epic sadface: Username and password do not match any user in this service"

    print("act Error: ",actErrorMsg)
    print("Exp Error: ", expErrorMsg)

    if actErrorMsg==expErrorMsg:
        print("TC Pass")
    else:
        print("TC Fail")
    time.sleep(5)

TC2_loginToSwagLabWithInvalidCredentials()