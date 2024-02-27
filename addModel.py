import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from datetime import datetime
from login import login
import time
model_url = 'https://d1lojwke7j5vfp.cloudfront.net/models/create'

chrome_options = webdriver.ChromeOptions()
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15'
chrome_options.add_argument(f'user-agent={user_agent}')

driver = webdriver.Chrome()
driver.implicitly_wait(1)

model_url = "https://d1lojwke7j5vfp.cloudfront.net/models/create"
model_name = "test_model"
training_job_name = "team45-mingjun-6"
try:
    # Log In
    login(driver)
    # Wait for login
    time.sleep(1)
    driver.get(model_url)
    page = driver.find_element(By.ID, 'root')
    inputs = page.find_elements(By.TAG_NAME, "input")
    name_input = inputs[0]
    training_job_input = inputs[1]
    name_input.send_keys(model_name+str(random.randint(1,9999999999)))
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





    


finally:
    # Close the browser window when done
    input("Press Enter to close the browser window.")
    driver.quit()

