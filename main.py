import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from datetime import datetime
from login import login
from addModel import add_model
from submitModel import submit_model
import time
model_url = 'https://d1lojwke7j5vfp.cloudfront.net/models/create'

chrome_options = webdriver.ChromeOptions()
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15'
chrome_options.add_argument(f'user-agent={user_agent}')

driver = webdriver.Chrome()
driver.implicitly_wait(2)

create_model_url = "https://d1lojwke7j5vfp.cloudfront.net/models/create"
model_name = "test_model"
training_job_name = "team45-mingjun-6"

submit_model_url = "https://d1lojwke7j5vfp.cloudfront.net/leaderboard"



try:
    # Log In
    login(driver)
    # Wait for login
    time.sleep(1)
    # This is for adding model
    # add_model(driver, create_model_url, model_name, training_job_name)
    submit_model(driver, submit_model_url)
    
    
    
   


    


finally:
    # Close the browser window when done
    input("Press Enter to close the browser window.")
    driver.quit()

