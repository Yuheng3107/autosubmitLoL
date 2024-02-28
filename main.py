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
    }
]

# Function to evaluate the model
def eval(username, password, alias, job):
    print(f"[{job}] Starting job")

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f'user-agent={USER_AGENT}')

    driver = webdriver.Chrome()
    driver.implicitly_wait(2)

    # Log In
    login(driver, username, password)
    time.sleep(1)

    # Add model
    # add_model(driver, MODEL_PREFIX, job)
    # time.sleep(1)

    # Submit model
    if (submit_model(driver, job) == False):
        driver.quit()
        return

    # for sanity, the driver quits and closes the chrome window while waiting for the job to finish.
    # if you want to keep the window open just comment out the lines between START_QUIET and END_QUIET

    # START_QUIET
    logout(driver)
    driver.quit()

    # Wait for 20 minutes
    for i in range(20):
        time.sleep(60)
        # prints every 4 minutes so as to not spam the console
        if (i % 4 == 0):
            print(f"[{job}] Waiting for job to finish | Time elapsed: {i+1} minutes")
    
    # Open the browser again
    driver = webdriver.Chrome()
    driver.implicitly_wait(2)
    login(driver, username, password)
    time.sleep(1)
    # END_QUIET

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


if __name__ == "__main__":
    main()

