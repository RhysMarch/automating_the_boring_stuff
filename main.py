from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import schedule

# This program will run every day at 23:59, as bookings are released at 00:00


def automated_booking():
    # ChromeDriver executable
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # Open the booking website
    driver.get(
        'https://sportsbookings.ncl.ac.uk/Connect/mrmLogin.aspx')
    driver.maximize_window()
    # Login
    login_button = driver.find_element(By.XPATH, '//*[@id="form_1"]/div[1]/div/a')
    login_button.click()
    second_login_button = driver.find_element(By.XPATH, '//*[@id="Authenticate"]/fieldset/div[1]/div[2]/a')
    second_login_button.click()
    # Enter username, password then login
    username_field = driver.find_element(By.ID, 'username')
    username_field.send_keys('c1012902')
    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys('ToneExperienceEnter18102002')
    final_login_button = driver.find_element(By.XPATH, '//*[@id="loginform"]/div[3]/button')
    final_login_button.click()
    # Load Volleyball Booking Page
    volleyball_button = driver.find_element(By.XPATH, '//*[@id="ctl00_MainContent__advanceSearchResultsUserControl_Activities_ctrl15_lnkActivitySelect_lg"]')
    volleyball_button.click()
    time.sleep(1)
    # Move ahead 14 days
    for i in range(14):
        next_button = driver.find_element(By.ID, 'ctl00_MainContent_Button2')
        next_button.click()


schedule.every().day.at("23:59").do(automated_booking)

