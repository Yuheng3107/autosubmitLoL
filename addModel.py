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
try:
    # Log In
    login(driver)
    # Wait for login
    time.sleep(1)
    driver.get(model_url)



    


finally:
    # Close the browser window when done
    input("Press Enter to close the browser window.")
    driver.quit()

