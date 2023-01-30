from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from rich import print
import time
import schedule
import json

# Username and password are stored in a json file, used for login process.
with open('config.json') as config_file:
    config = json.load(config_file)

username = config['username']
password = config['password']

# Print day and time program was started
print(time.strftime("%d %B %Y %H:%M:%S") + " - Program Started")


def automated_booking():
    print(time.strftime("%d %B %Y %H:%M:%S") + " - Booking Process Started")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # ChromeDriver executable
    driver.get('https://sportsbookings.ncl.ac.uk/Connect/mrmLogin.aspx')  # Open booking website

    # Login buttons
    driver.find_element(By.XPATH, '//*[@id="form_1"]/div[1]/div/a').click()
    driver.find_element(By.XPATH, '//*[@id="Authenticate"]/fieldset/div[1]/div[2]/a').click()

    # Enter username and password, then login
    username_field = driver.find_element(By.ID, 'username')
    username_field.send_keys(username)
    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys(password)
    final_login_button = driver.find_element(By.XPATH, '//*[@id="loginform"]/div[3]/button')
    final_login_button.send_keys(Keys.RETURN)

    # Load Volleyball Booking Page
    driver.find_element(By.XPATH, '//*[@id="ctl00_MainContent__advanceSearchResultsUserControl_Activities_ctrl15_lnkActivitySelect_lg"]').click()
    time.sleep(1)

    # Move ahead 2 weeks (New bookings are released 14 days from now)
    for i in range(14):
        driver.find_element(By.ID, 'ctl00_MainContent_Button2').click()

    # Wait until 00:00:00, then refresh page to load new bookings
    while time.strftime("%H:%M:%S") != "00:00:00":
        time.sleep(1)
    driver.refresh()
    time.sleep(0.5)
    print(time.strftime("%d %B %Y %H:%M:%S") + """ - Page Refreshed
    
----------------------------""")

    # ----------------------------------------------------------------------------------------- #
    # //*[@id="ctl00_MainContent_grdResourceView"]/tbody/tr[7]/td/input xpath for 12:00 button  #
    # //*[@id="ctl00_MainContent_grdResourceView"]/tbody/tr[16]/td/input xpath for 21:00 button #
    # ----------------------------------------------------------------------------------------- #

    xpath_base = '//*[@id="ctl00_MainContent_grdResourceView"]/tbody/tr['

    # Checks 21:00 booking then works down to 12:00, will pick the first available booking
    for slot in range(16, 6, -1):
        xpath = xpath_base + str(slot) + ']/td/input'
        try:
            driver.find_element(By.XPATH, xpath).click()
            print("| " + str(slot + 5) + ":00 slot taken |")
        except:
            print("| " + str(slot + 5) + ":00 slot not available |")

    # Click the confirm button to take the booking, if no booking is available, the program will go back to waiting for the next day.
    try:
        print("----------------------------")
        driver.find_element(By.XPATH, '//*[@id="ctl00_MainContent_btnBasket"]').click()
    except:
        print("""----------------------------
        
    No booking available.
    Waiting for next day.
    
    """)

    # Close the browser
    driver.close()


# Program idles, until 23:59:59, then starts the booking process.
try:
    schedule.every().day.at("23:59").do(automated_booking)
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    print(time.strftime("%d %B %Y %H:%M:%S") + " - Program Stopped")
