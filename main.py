from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# ChromeDriver executable
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the booking website
driver.get("https://sportsbookings.ncl.ac.uk/Connect/mrmLogin.aspx")
driver.maximize_window()
