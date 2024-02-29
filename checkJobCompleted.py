import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import LEADERBOARD_URL

def check_job_completed(driver) -> bool:
    driver.get(LEADERBOARD_URL)

    # Specify the maximum amount of time to wait for the condition (in seconds)
    timeout = 20

    # Use WebDriverWait to wait for the leaderboard to be loaded (leaderboard is the last to load, 
    # so we can be sure that everything else is loaded by the time the leaderboard is loaded)
    wait = WebDriverWait(driver, timeout)
    _ = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "awsui_content_5gtk3_lh8g2_129")))
    no_pending_submission = driver.find_elements(By.CSS_SELECTOR, 'div[data-itemid="no_pending_submission_leaderboard"]')
    return True if no_pending_submission else False