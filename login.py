import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import BASE_URL

def login(driver, username: str, password: str):
    # Open the website in the browser
    driver.get(BASE_URL)

    timeout = 20
    wait = WebDriverWait(driver, timeout)
    page = wait.until(EC.presence_of_element_located((By.ID, 'root')))

    # Need use root as reference, rest is blocked somehow
    username_input = page.find_element(By.ID, 'Username')
    password_input = page.find_element(By.ID, 'Password')
    buttons = driver.find_elements(By.TAG_NAME, "button")
    button = buttons[2]
    username_input.send_keys(username)
    password_input.send_keys(password)
    button.click()
    print(f"logged into {username} account successfully")
    # Finished logging in