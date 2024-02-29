import threading
from selenium import webdriver
from login import login
from addModel import add_model
from submitModel import submit_model
from readData import read_data
from checkJobCompleted import check_job_completed
from logout import logout
from log import log
import time

# Constants
MODEL_PREFIX            = 'test_model'
USER_AGENT              = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15'

# How many times to run each eval job
ITERATION_COUNT         = 8

<<<<<<< HEAD

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
=======
# Add your runs here
runs = [
    {
        "username": "mong",
        "password": "P@$$w0rd20021212",
        "alias": "team45-mingjun",
        "job": "team45-mingjun-6"
    },
    {
        "username": "AppleJem",
        "password": "AWS_pa55word",
        "alias": "team45-mingjun",
        "job": "team45-mingjun-7"
>>>>>>> d8b7af5b4774dd6530471131c0ca05cef7104c59
    }
    for i in range(len(usernames))
]
<<<<<<< HEAD
is_logging = True
=======

# Function to evaluate the model
>>>>>>> d8b7af5b4774dd6530471131c0ca05cef7104c59
def eval(username, password, alias, job):
    print(f"[{job}] Starting job")

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f'user-agent={USER_AGENT}')

    driver = webdriver.Chrome()
    driver.implicitly_wait(2)
    print(job)
    # Log In
    login(driver, username, password)
    time.sleep(1)

    # Add model
<<<<<<< HEAD
    add_model(driver, create_model_url, job)
    time.sleep(2)

    # Submit model
    #submit_model(driver, submit_model_url, job)

    if is_logging:
        read_data(driver, read_leaderboard_url, alias)
    time.sleep(2)

    # Log Out
    logout(driver)

=======
    # add_model(driver, MODEL_PREFIX, job)
    # time.sleep(1)

    # Submit model
    if (submit_model(driver, job) == False):
        driver.quit()
        return
>>>>>>> d8b7af5b4774dd6530471131c0ca05cef7104c59

    # for sanity, the driver quits and closes the chrome window while waiting for the job to finish.
    # if you want to keep the window open just comment out the lines between START_QUIET and END_QUIET

    # START_QUIET
    logout(driver)
    driver.quit()

    # Wait for 20 minutes
<<<<<<< HEAD
    for i in range(17):
=======
    for i in range(20):
>>>>>>> d8b7af5b4774dd6530471131c0ca05cef7104c59
        time.sleep(60)
        # prints every 4 minutes so as to not spam the console
        if (i % 4 == 0):
            print(f"[{job}] Waiting for job to finish | Time elapsed: {i+1} minutes")
    
<<<<<<< HEAD
=======
    # Open the browser again
    driver = webdriver.Chrome()
    driver.implicitly_wait(2)
    login(driver, username, password)
    time.sleep(1)
    # END_QUIET
>>>>>>> d8b7af5b4774dd6530471131c0ca05cef7104c59

    # Read the leaderboard
    for i in range(10):
        if i == 9:
            print(f"[{job}] Job still has not finished yet after {i+1} additional minutes. This driver will quit now.")
        else:
            if (check_job_completed(driver)):
                read_data(driver, alias)
                break
            else:
                print(f"[{job}] Job has not finished yet. Waiting for 1 minute.")
                time.sleep(60)
    
<<<<<<< HEAD


def main():
    for run in runs:
        # Create a tuple of values from the dictionary
        args_tuple = (run["username"], run["password"], run["alias"], run["job"])
        t = threading.Thread(target=eval, args=args_tuple)
        t.start()
        
=======
    time.sleep(1)
    driver.quit()


def main():
    for i in range(ITERATION_COUNT):
        print(f"Starting iteration {i}")
        threads = []  # List to keep track of thread objects
        for run in runs:
            # Create a tuple of values from the dictionary
            args_tuple = (run["username"], run["password"], run["alias"], run["job"])
            t = threading.Thread(target=eval, args=args_tuple)
            t.start()
            threads.append(t)

        # Wait for all threads in this iteration to complete
        for t in threads:
            t.join()
>>>>>>> d8b7af5b4774dd6530471131c0ca05cef7104c59


if __name__ == "__main__":
    main()

