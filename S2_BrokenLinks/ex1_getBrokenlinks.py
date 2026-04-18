from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

driver = webdriver.Chrome()
driver.get("https://demoqa.com/broken")

allLinks = driver.find_elements(By.TAG_NAME, "a")

for link in allLinks:
    url = link.get_attribute("href")

    if url is None or url == "":
        continue

    try:
        response = requests.get(url)
        if response.status_code >= 400:
            print(f"Broken link: {url} --> {response.status_code}")
        else:
            print(f"Valid link: {url}")
    except:
        print(f"Error checking: {url}")

driver.quit()