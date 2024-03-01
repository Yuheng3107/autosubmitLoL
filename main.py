import threading
from selenium import webdriver
from login import login
from addModel import add_model, record_model
from submitModel import submit_model
from readData import read_data
from checkJobCompleted import check_job_completed
from logout import logout
from log import log
import time
from analyse import analyse

# Constants
MODEL_PREFIX            = 'test_model'
USER_AGENT              = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15'

# How many times to run each eval job
ITERATION_COUNT         = 8


usernames = ['test_account', 'test_account1', 'test_account2', 'test_account3', 'test_account4', 'test_account5', 'test_account6', 'test_account7', 'test_account8', 'test_account9']
passwords = ['Password1234!', 'Password1234!', 'Password1234!', 'Password1234!', 'Password1234!', 'Password1234!', 'Password1234!', 'Password1234!', 'Password1234!', 'Password1234!']
aliases = ['team45_yh', 'team45_yuheng', 'team45_kyh', 'team45_yhb', 'team_45_yhb2', 'team_45_yhb3', 'T45_yh_lepaks', 'T45_yh_lepaking', 'team_45_winner', 'team_45_slacker']
jobs = ["team45-mingjun-15v2" for i in range(10)]
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
    print(f"[{job}] Starting job")

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(2)
    # Log In
    login(driver, username, password)
    time.sleep(1)
    # Add model
    add_model(driver, job)
    time.sleep(2)


    # Submit model
    submit_model(driver, job)
    time.sleep(2)
    read_data(driver, alias)
    time.sleep(2)
    # Log Out
    logout(driver)
    time.sleep(1)
    analyse()

    # for sanity, the driver quits and closes the chrome window while waiting for the job to finish.
    # if you want to keep the window open just comment out the lines between START_QUIET and END_QUIET
    
    time.sleep(2)
    # START_QUIET
    driver.quit()

    # Read the leaderboard
    # for i in range(10):
    #     if i == 9:
    #         print(f"[{job}] Job still has not finished yet after {i+1} additional minutes. This driver will quit now.")
    #     else:
    #         if (check_job_completed(driver)):
    #             read_data(driver, alias)
    #             break
    #         else:
    #             print(f"[{job}] Job has not finished yet. Waiting for 1 minute.")
    #             time.sleep(60)

    
    

    
    


def main():
    for i in range(2000):
        # Wait for 20 minutes
        if i != 0:
            for i in range(17):
                time.sleep(60)      
            
        for run in runs:
            # Create a tuple of values from the dictionary
            args_tuple = (run["username"], run["password"], run["alias"], run["job"])
            t = threading.Thread(target=eval, args=args_tuple)
            t.start()
        
        


if __name__ == "__main__":
    main()

