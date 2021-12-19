from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "/Users/ychang3/Desktop/yuan/project/python/webAuto/chromedriver"
EMAIL = ""
PWD = ""
SEARCH_KEY = "#華航"

driver = webdriver.Chrome(PATH)
driver.get("https://www.instagram.com/accounts/login/")

try:
    fbLoginBtn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "yWX7d"))
    )
    fbLoginBtn.click()

    emailField = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "email"))
    )
    pwdField = driver.find_element(By.ID, "pass")
    loginBtn = driver.find_element(By.ID, "loginbutton")

    emailField.clear()
    pwdField.clear()

    emailField.send_keys(EMAIL)
    pwdField.send_keys(PWD)

    loginBtn.click()

    # Dismiss popup
    popupBtn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "HoLwm"))
    )
    popupBtn.click()

    # Should be in IG now

    # Find the search field
    searchField = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "x3qfX"))
    )
    searchField.clear()
    searchField.send_keys(SEARCH_KEY)

    # Click two times enter to start the search
    sleep(2)
    searchField.send_keys(Keys.RETURN)
    sleep(2)
    searchField.send_keys(Keys.RETURN)

    # Find images
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "Saeqz"))
    )
    images = driver.find_elements(By.CLASS_NAME, "FFVAD")
    for image in images:
        print(image.get_attribute("src"))

finally:
    # driver.quit()
    print("Something wrong happen !")
