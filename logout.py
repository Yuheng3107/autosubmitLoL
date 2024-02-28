import time
from selenium.webdriver.common.by import By

def logout(driver):
    driver.get("https://d1lojwke7j5vfp.cloudfront.net/")
    time.sleep(1)
    buttons = driver.find_elements(By.TAG_NAME, 'button')
    test_account_button = buttons[1]
    test_account_button.click()
    time.sleep(1)
    list_elements = driver.find_elements(By.TAG_NAME, "li")
    sign_out_button = list_elements[0]
    sign_out_button.click()