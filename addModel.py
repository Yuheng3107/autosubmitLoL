import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from urls import MODEL_REGISTRATION_URL, MODELS_URL
import time
from log import log
import csv


chrome_options = webdriver.ChromeOptions()
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15'
chrome_options.add_argument(f'user-agent={user_agent}')


def add_model(driver, training_job_name: str):
    driver.get(MODEL_REGISTRATION_URL)
    page = driver.find_element(By.ID, 'root')
    inputs = page.find_elements(By.TAG_NAME, "input")
    name_input = inputs[0]
    training_job_input = inputs[1]
    name = training_job_name+str(random.randint(1,9999999999))
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

    # Functionality to record model
    record_model(driver, name, training_job_name)

def record_model(driver, model_name: str, training_job_name: str):
    """This fuction records the model_name and the corresponding training job in the log files"""
    driver.get(MODELS_URL)
    inputs = driver.find_elements(By.TAG_NAME, "input")
    search_input = inputs[0]
    search_input.send_keys(model_name)
    time.sleep(2)
    headers = driver.find_elements(By.TAG_NAME, "th")
    for header in headers:
        if header.text == model_name:
            model_id = header.find_element(By.XPATH, "following-sibling::*[2]")
            time.sleep(1)
            with open("models.csv", "a") as f:
                writer = csv.writer(f)
                rows = [training_job_name, model_id.text]
                writer.writerow(rows)



