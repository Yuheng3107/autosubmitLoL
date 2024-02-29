import threading
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


usernames = ['test_account', 'test_account1', 'test_account2', 'test_account3', 'test_account4', 'test_account5']
passwords = ['Password1234!', 'Password1234!', 'Password1234!', 'Password1234!', 'Password1234!', 'Password1234!']
aliases = ['team45_yh', 'team45_yuheng', 'team45_kyh', 'team45_yhb', 'team_45_yhb2', 'team_45_yhb3']
jobs = ["team45-mingjun-4",
"team45-mingjun-5",
"team45-mingjun-6",
"team45-mingjun-7",
"team45-mingjun-8",
"team45-mingjun-9"]
runs = [
    {
        "username": usernames[i],
        "password": passwords[i],
        "alias": aliases[i],
        "job": jobs[i]
    }
    for i in range(len(usernames))
]
is_logging = True
def eval(username, password, alias, job):
    chrome_options = webdriver.ChromeOptions()
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15'
    chrome_options.add_argument(f'user-agent={user_agent}')

    driver = webdriver.Chrome()
    driver.implicitly_wait(2)
    print(job)
    # Log In
    login(driver, username, password)
    time.sleep(2)

    # Add model
    add_model(driver, create_model_url, job)
    time.sleep(2)

    # Submit model
    #submit_model(driver, submit_model_url, job)

    if is_logging:
        read_data(driver, read_leaderboard_url, alias)
    time.sleep(2)

    # Log Out
    logout(driver)


    # for sanity, the driver quits and closes the chrome window while waiting for the job to finish.
    # if you want to keep the window open just comment out the lines between START_QUIET and END_QUIET

    # START_QUIET
    driver.quit()

    # Wait for 20 minutes
    for i in range(17):
        time.sleep(60)
        # prints every 4 minutes so as to not spam the console
        if (i % 4 == 0):
            print(f"Waiting for job to finish: {job} | Time elapsed: {i+1} minutes")
    


    


def main():
    for run in runs:
        # Create a tuple of values from the dictionary
        args_tuple = (run["username"], run["password"], run["alias"], run["job"])
        t = threading.Thread(target=eval, args=args_tuple)
        t.start()
        
        
        


if __name__ == "__main__":
    main()

