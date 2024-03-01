import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from urls import LEADERBOARD_URL
from get_time import get_time

def submit_model(driver, training_job_name: str) -> bool:
    """Submits the model based on the training job name"""
    driver.get(LEADERBOARD_URL)

    timeout = 20
    wait = WebDriverWait(driver, timeout)
    submit_model_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(., '+ Submit your model')]")))
    if submit_model_button.get_attribute("disabled"):
        print(f"[{training_job_name}] The submit button is disabled. That means another job is still running. Please wait for it to finish. This function will exit now")
        return False
    submit_model_button.click()

    time.sleep(1)
    buttons = driver.find_elements(By.TAG_NAME, "button")
    # Choose model button is 5
    choose_model_button = buttons[5]
    choose_model_button.click()
    time.sleep(1)
    next_button = buttons[7]
    time.sleep(1)
    list_elements = driver.find_elements(By.TAG_NAME, "li")
    # element with index 9 is the newest model
    button = None
    for i, element in enumerate(list_elements):
        if training_job_name in str(element.text):
            button = element
            break
    button.click()
    next_button.click()
    time.sleep(1)
    buttons = driver.find_elements(By.TAG_NAME, "button")
    submit_button = buttons[8]
    submit_button.click()
    print(f"[{get_time()}] Submitted model {training_job_name}")
    return True

    
    
    
    
   


    


