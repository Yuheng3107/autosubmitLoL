import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from urls import MODEL_REGISTRATION_URL
import time

<<<<<<< HEAD

chrome_options = webdriver.ChromeOptions()
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15'
chrome_options.add_argument(f'user-agent={user_agent}')


def add_model(driver, create_model_url: str, training_job_name: str):
    driver.get(create_model_url)
=======
def add_model(driver, model_name: str, training_job_name: str):
    driver.get(MODEL_REGISTRATION_URL)
>>>>>>> d8b7af5b4774dd6530471131c0ca05cef7104c59
    page = driver.find_element(By.ID, 'root')
    inputs = page.find_elements(By.TAG_NAME, "input")
    name_input = inputs[0]
    training_job_input = inputs[1]
<<<<<<< HEAD
    name = training_job_name+str(random.randint(1,9999999999))
=======
    name = model_name+"_"+str(random.randint(1,9999999999))
>>>>>>> d8b7af5b4774dd6530471131c0ca05cef7104c59
    name_input.send_keys(name)
    training_job_input.send_keys(training_job_name)
    buttons = driver.find_elements(By.TAG_NAME, "button")
    """for i, button in enumerate(buttons):
        print(i, button.text)"""
    # Button w index 6 is next
    next_button = buttons[6]
    next_button.click()
    time.sleep(1)
    buttons = driver.find_elements(By.TAG_NAME, "button")
    # Register model button is button 8
    register_model_button = buttons[8]
    register_model_button.click()    
