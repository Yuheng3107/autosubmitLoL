from selenium import webdriver
from login import login
from addModel import add_model
from submitModel import submit_model
from readData import read_data
from log import log
from logout import logout
import time
model_url = 'https://d1lojwke7j5vfp.cloudfront.net/models/create'

create_model_url = "https://d1lojwke7j5vfp.cloudfront.net/models/create"
model_name = "test_model"
training_job_name = "team45-mingjun-4"

submit_model_url = "https://d1lojwke7j5vfp.cloudfront.net/leaderboard"

read_leaderboard_url = "https://d1lojwke7j5vfp.cloudfront.net/leaderboard"
# Account Name is needed for bot to search your name to find your result
account_name = "team45_yh"

username = 'test_account'
password = 'Password1234!'

usernames = ['test_account', 'test_account1', 'test_account2', 'test_account3', 'test_account4', 'test_account5']
passwords = ['Password1234!', 'Password1234!', 'Password1234!', 'Password1234!', 'Password1234!', 'Password1234!']
account_names = ['team45_yh', 'team45_yuheng', 'team45_kyh', 'team45_yhb', 'team_45_yhb2', 'team_45_yhb3']
models = ["team45-mingjun-4",
"team45-mingjun-5",
"team45-mingjun-6",
"team45-mingjun-7",
"team45-mingjun-8",
"team45-mingjun-9"]
is_logging = True
def main():
    if len(usernames) != len(passwords) or len(usernames) != len(account_names) or len(usernames) < len(models):

        print("Make sure usernames, passwords and account names have the same length")
        return

    chrome_options = webdriver.ChromeOptions()
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15'
    chrome_options.add_argument(f'user-agent={user_agent}')

    driver = webdriver.Chrome()
    driver.implicitly_wait(2)

    try:
        for i in range(len(models)):
            if i in [0,1,2,3]:
                continue
            username = usernames[i]
            password = passwords[i]
            account_name = account_names[i]
            training_job_name = models[i]
            # Log In
            login(driver, username, password)
            # Wait for login
            time.sleep(1)
            # This is for adding model
            #add_model(driver, create_model_url, model_name, training_job_name)
            time.sleep(1)
            submit_model(driver, submit_model_url, training_job_name)
            if is_logging:
                read_data(driver, read_leaderboard_url, account_name)
            # # Need logout function
            time.sleep(1)
            logout(driver)
            

        

    finally:
        # Close the browser window when done
        input("Press Enter to close the browser window.")
        driver.quit()

for i in range(20):
    main()
    for i in range(16):
        print(f"Minute: {i+1}")
        time.sleep(60)

