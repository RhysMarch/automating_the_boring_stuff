from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import schedule
import logging
import json

# This program will run every day at 23:59, as bookings are released at 00:00

with open('config.json') as config_file:
    config = json.load(config_file)

username = config['username']
password = config['password']


def automated_booking():
    print("Starting automated booking")
    # ChromeDriver executable
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # Open the booking website
    driver.get('https://sportsbookings.ncl.ac.uk/Connect/mrmLogin.aspx')
    driver.maximize_window()

    # Login
    login_button = driver.find_element(By.XPATH, '//*[@id="form_1"]/div[1]/div/a')
    login_button.click()
    second_login_button = driver.find_element(By.XPATH, '//*[@id="Authenticate"]/fieldset/div[1]/div[2]/a')
    second_login_button.click()

    # Enter username, password then login
    username_field = driver.find_element(By.ID, 'username')
    username_field.send_keys(username)
    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys(password)
    final_login_button = driver.find_element(By.XPATH, '//*[@id="loginform"]/div[3]/button')
    final_login_button.send_keys(Keys.RETURN)

    # Load Volleyball Booking Page
    volleyball_button = driver.find_element(By.XPATH, '//*[@id="ctl00_MainContent__advanceSearchResultsUserControl_Activities_ctrl15_lnkActivitySelect_lg"]')
    volleyball_button.click()
    time.sleep(1)  # This sleep is necessary to allow the page to load

    # Move ahead 14 days
    for i in range(14):
        next_button = driver.find_element(By.ID, 'ctl00_MainContent_Button2')
        next_button.click()

    # Select the best available slot (I don't want 9am slots lol)
    # TODO: Implement automation to select the best available slot


# Runs the program every day at 23:59
try:
    schedule.every().day.at("23:59").do(automated_booking)
    while True:
        schedule.run_pending()  # Constantly checks if it's time to run the program
        print("Running")
        time.sleep(1)
except Exception as e:
    logging.exception("An error occurred: %s" % e)

