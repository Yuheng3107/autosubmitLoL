import csv
from selenium.webdriver.common.by import By
import time
from urls import LEADERBOARD_URL

def read_data(driver, account_name: str):
    """This function reads data from the leaderboard and appends it to the logfile
    If you haven't submitted anything do not run this function
    """
    driver.get(LEADERBOARD_URL)
    # Make sure the job has completed
    
    page = driver.find_element(By.ID, 'root')
    # Need use root as reference, rest is blocked somehow
    input_element = page.find_element(By.TAG_NAME, 'input')
    input_element.send_keys(account_name)
    time.sleep(5)
    data = driver.find_elements(By.TAG_NAME, "td")
    # Index 4 is last submitted win rate, 5 is no of wins, 6 is no of draws, 7 is no of total runs

    model_id = data[1].text
    last_submitted_win_rate = data[4].text
    win_count = data[5].text
    draw_count = data[6].text
    total_runs = data[7].text
    # Make csv of model mappings into dict
    model_name = "NULL"
    with open('models.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Model Id"] == model_id:
                model_name = row["Training Job Name"]
    new_data = [model_name, last_submitted_win_rate, win_count, draw_count, total_runs]
    with open('./logfile.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(new_data)






    
    
   


    



