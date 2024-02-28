import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from urls import MODEL_REGISTRATION_URL
import time

def add_model(driver, model_name: str, training_job_name: str):
    driver.get(MODEL_REGISTRATION_URL)
    page = driver.find_element(By.ID, 'root')
    inputs = page.find_elements(By.TAG_NAME, "input")
    name_input = inputs[0]
    training_job_input = inputs[1]
    name = model_name+"_"+str(random.randint(1,9999999999))
    name_input.send_keys(name)
    training_job_input.send_keys(training_job_name)
    buttons = driver.find_elements(By.TAG_NAME, "button")
    """for i, button in enumerate(buttons):
        print(i, button.text)"""
    # Button w index 6 is next
    next_button = buttons[6]
    next_button.click()
    time.sleep(0.1)
    buttons = driver.find_elements(By.TAG_NAME, "button")
    # Register model button is button 8
    register_model_button = buttons[8]
    register_model_button.click()    
    # Want to add functionality to register model Id and training job name
    #driver.get()

def record_model(model_name):
    pass