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

runs = [
    {
        "username": "mong",
        "password": "P@$$w0rd20021212",
        "alias": "team45-mingjun",
        "job": "team45-mingjun-6"
    }
]

is_logging = True
def eval(username, password, alias, job):
    chrome_options = webdriver.ChromeOptions()
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15'
    chrome_options.add_argument(f'user-agent={user_agent}')

    driver = webdriver.Chrome()
    driver.implicitly_wait(2)

    # Log In
    login(driver, username, password)
    time.sleep(2)

    # Add model
    # add_model(driver, create_model_url, model_name, job)
    # time.sleep(2)

    # Submit model
    # submit_model(driver, submit_model_url, job)


    # for sanity, the driver quits and closes the chrome window while waiting for the job to finish.
    # if you want to keep the window open just comment out the lines between START_QUIET and END_QUIET

    # START_QUIET
    logout(driver)
    driver.quit()

    # Wait for 20 minutes
    for i in range(20):
        time.sleep(1)
        # prints every 4 minutes so as to not spam the console
        if (i % 4 == 0):
            print(f"Waiting for job to finish: {job} | Time elapsed: {i+1} minutes")
    
    # Open the browser again
    driver = webdriver.Chrome()
    driver.implicitly_wait(2)
    login(driver, username, password)
    time.sleep(2)
    # END_QUIET

    # Read the leaderboard
    read_data(driver, read_leaderboard_url, alias)
    time.sleep(2)
    
    driver.quit()


def main():
    for run in runs:
        # Create a tuple of values from the dictionary
        args_tuple = (run["username"], run["password"], run["alias"], run["job"])
        t = threading.Thread(target=eval, args=args_tuple)
        t.start()


if __name__ == "__main__":
    main()

