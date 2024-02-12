import time
import json
import schedule
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from rich import print
from webdriver_manager.chrome import ChromeDriverManager

# Username and password are stored in a json file, used for login process.
with open('config.json') as config_file:
    config = json.load(config_file)

username = config['username']
password = config['password']

# Print day and time program was started
print(time.strftime("%d %B %Y %H:%M:%S") + " - Program Started")


def automated_booking():
    print(time.strftime("%d %B %Y %H:%M:%S") + " - Booking Process Started")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        driver.get('https://sportsbookings.ncl.ac.uk/Connect/mrmLogin.aspx')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    except Exception as e:
        print(f"Error navigating to the URL: {e}")

    # Login buttons
    try:
        driver.find_element(By.XPATH, '//*[@id="form_1"]/div[1]/div/a').click()
        driver.find_element(By.XPATH, '//*[@id="Authenticate"]/fieldset/div[1]/div[2]/a').click()

        # Enter username and password, then login
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@id="i0116"]')))
        username_field = driver.find_element(By.XPATH, '//input[@id="i0116"]')
        username_field.send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()  # Click the next button

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@id="i0118"]')))
        password_field = driver.find_element(By.XPATH, '//input[@id="i0118"]')
        password_field.send_keys(password)
        time.sleep(2)
        driver.find_element(By.ID, "idSIButton9").click()
    except TimeoutException:
        print("Timed out waiting for page elements to load")

    print("Please complete the authentication. Waiting for completion...")

    # Element XPATH
    auth_element_xpath = '//*[@id="idRichContext_DisplaySign"]'

    # Wait for the authentication element to be visible
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, auth_element_xpath)))
    except TimeoutException:
        print("Authentication prompt not found or timed out.")
        driver.quit()
        return

    # Loop until the element is no longer visible
    while True:
        try:
            # Check if the element is still visible
            element = driver.find_element(By.XPATH, auth_element_xpath)
            if not element.is_displayed():
                print("Authentication complete. Continuing with the process.")
                break
        except:
            # If element is not found or not visible, break the loop
            print("Authentication complete. Continuing with the process.")
            break
        time.sleep(1)  # Delay to prevent too frequent checks

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "idSIButton9")))
    driver.find_element(By.ID, "idSIButton9").click()

    # Load Volleyball Booking Page
    try:
        # Wait for the first element to be clickable and then click
        recent_bookings = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="recentbookings"]/div[1]/div[1]'))
        )
        recent_bookings.click()

        # Wait for the Volleyball Booking Page link to be clickable and then click
        volleyball_booking_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="ctl00_MainContent_MostRecentBookings1_Bookings_ctl01_bookingLink"]'))
        )
        volleyball_booking_link.click()
    except TimeoutException:
        print("Timed out waiting for the elements to be clickable.")
    except Exception as e:
        print(f"An error occurred: {e}")

    # Move ahead 2 weeks (New bookings are released 14 days from now)
    try:
        # Wait for the element to be present and click the first time
        forward_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_MainContent_dateForward1"]'))
        )
        forward_button.click()

        time.sleep(1)

        # Wait for the element to be present again and click the second time
        forward_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_MainContent_dateForward1"]'))
        )
        forward_button.click()
    except TimeoutException:
        print("Timed out waiting for the element to be present.")
        # Handle the exception (e.g., retry, exit, etc.)
    except Exception as e:
        print(f"An error occurred: {e}")
        # Handle other exceptions

    # Wait until 00:00:00, then refresh page to load new bookings
    while time.strftime("%H:%M:%S") != "00:00:00":
        time.sleep(1)
    driver.refresh()
    time.sleep(0.5)
    print(time.strftime("%d %B %Y %H:%M:%S") + """ - Page Refreshed
    
----------------------------""")

    time_slots_xpaths = {
        "21:00": '//*[@id="ctl00_MainContent_cal_calbtn98"]',
        "20:00": '//*[@id="ctl00_MainContent_cal_calbtn91"]',
        "19:00": '//*[@id="ctl00_MainContent_cal_calbtn84"]',
        "18:00": '//*[@id="ctl00_MainContent_cal_calbtn77"]',
        "17:00": '//*[@id="ctl00_MainContent_cal_calbtn70"]',
        "16:00": '//*[@id="ctl00_MainContent_cal_calbtn63"]',
        "15:00": '//*[@id="ctl00_MainContent_cal_calbtn56"]',
        "14:00": '//*[@id="ctl00_MainContent_cal_calbtn49"]',
        "13:00": '//*[@id="ctl00_MainContent_cal_calbtn42"]',
        "12:00": '//*[@id="ctl00_MainContent_cal_calbtn35"]'
    }

    # Loop through the time slots from 21:00 to 12:00
    for slot, xpath in time_slots_xpaths.items():
        try:
            driver.find_element(By.XPATH, xpath).click()
            print(f"| {slot} slot taken         |")
        except:
            print(f"| {slot} slot not available |")

    # Click the confirm button to take the booking
    try:
        driver.find_element(By.XPATH, '//*[@id="ctl00_MainContent_btnBasket"]').click()
        print("----------------------------")
    except:
        print("""----------------------------

    No booking available.
    Waiting for next day.

    """)

    # Close the browser
    driver.close()


# Program idles, until 23:59, then starts the booking process.
try:
    schedule.every().day.at("23:59").do(automated_booking)
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    print(time.strftime("%d %B %Y %H:%M:%S") + " - Program Stopped")
