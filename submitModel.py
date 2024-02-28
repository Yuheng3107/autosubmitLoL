import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from datetime import datetime
import time


def submit_model(driver, submit_model_url: str):
    driver.get(submit_model_url)
    time.sleep(1)
    buttons = driver.find_elements(By.TAG_NAME, "button")
    # Button index 5 is submit model button
    submit_model_button = buttons[5]
    submit_model_button.click()
    time.sleep(1)
    buttons = driver.find_elements(By.TAG_NAME, "button")
    # Choose model button is 5
    choose_model_button = buttons[5]
    choose_model_button.click()
    time.sleep(1)
    next_button = buttons[7]
    list_elements = driver.find_elements(By.TAG_NAME, "li")
    # element with index 9 is the newest model
    button = list_elements[9]
    button.click()
    next_button.click()
    time.sleep(1)
    buttons = driver.find_elements(By.TAG_NAME, "button")
    submit_button = buttons[8]
    submit_button.click()

    
    
    
    
   


    

