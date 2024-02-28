from selenium import webdriver
from login import login
from addModel import add_model
from submitModel import submit_model
from readData import read_data
import time
model_url = 'https://d1lojwke7j5vfp.cloudfront.net/models/create'

create_model_url = "https://d1lojwke7j5vfp.cloudfront.net/models/create"
model_name = "test_model"
training_job_name = "team45-mingjun-6"

submit_model_url = "https://d1lojwke7j5vfp.cloudfront.net/leaderboard"

read_leaderboard_url = "https://d1lojwke7j5vfp.cloudfront.net/leaderboard"
# Account Name is needed for bot to search your name to find your result
account_name = "team45-yh"

username = 'test_acc'
password = 'Password1234!'
def main():
    chrome_options = webdriver.ChromeOptions()
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15'
    chrome_options.add_argument(f'user-agent={user_agent}')

    driver = webdriver.Chrome()
    driver.implicitly_wait(2)

    try:
        # for i in range(20):
            
        #     login(driver, username, password)
        #     time.sleep(1)
        #     submit_model(driver, submit_model_url)
        #     time.sleep(16*60)


        # Log In
        login(driver, username, password)
        # Wait for login
        time.sleep(1)
        # This is for adding model
        #add_model(driver, create_model_url, model_name, training_job_name)
        submit_model(driver, submit_model_url)
        read_data(driver, read_leaderboard_url, account_name)

    finally:
        # Close the browser window when done
        input("Press Enter to close the browser window.")
        driver.quit()

for i in range(20):
    main()
    for i in range(17):
        print(f"Minute: {i+1}")
        time.sleep(60)

