from selenium.webdriver.common.by import By
import time

login_url = 'https://d1lojwke7j5vfp.cloudfront.net/'


def login(driver, username: str, password: str):
    # Open the website in the browser
    driver.get(login_url)
    time.sleep(1)
    page = driver.find_element(By.ID, 'root')
    # Need use root as reference, rest is blocked somehow
    username_input = page.find_element(By.ID, 'Username')
    password_input = page.find_element(By.ID, 'Password')
    buttons = driver.find_elements(By.TAG_NAME, "button")
    button = buttons[2]
    username_input.send_keys(username)
    password_input.send_keys(password)
    button.click()
    # Finished logging in