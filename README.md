# Court Booking Automation
This is a personal project and isn't intended to be used by people other than me. 

This script automates volleyball court bookings released at midnight. 
It requires Microsoft Authenticator for login, necessitating human intervention. 
The rest of the process is automated.

The script only works when I authenticate the 2FA login. This ensures fairness as I'm actively involved in the process. 
Also, the script doesn't impact my booking success, as I'd achieve the same results manually.

<br>

## Your Details for Config.json Settings 

- `email`: This is the email address used for logging into the NCL booking system. It's the username part of your credentials for accessing the booking platform.

- `password`: This is the password associated with your email for the NCL booking system.

- `sender-email`: This is the email address used to send notifications. It's the "From" address in the emails that the script sends. 

- `recipient-email`: This is the email address where you want to receive notifications. It's the "To" address in the emails. This could be the same as `sender-email` if you're sending notifications to yourself.

<br>


## How to Use  

1. Ensure Python is installed on your system. You can download it from [Python's official website](https://www.python.org/downloads/).

2. **Install Requirements**: First, make sure to install all the required packages listed in the `requirements.txt` file. This can typically be done using a command like `pip install -r requirements.txt` in your terminal.

3. **Configure Your Details**: Open the `config.json` file and input your details.

### Running the Script

3. **Execute the Script**: Run the python file (e.g., `python court_booking.py`). This starts the script.

4. **Automated Checking**: The script will continuously check the time until it reaches 23:30.

5. **Booking Process Initiation**: At exactly 23:30, the automated booking process begins.

6. **Automated Login and Booking**: 
   - The script navigates to the booking URL.
   - It then logs in using the credentials provided in the `config.json` file.
   - You are required to authenticate the login through Microsoft Authenticator.
     - The authentication number is sent to your email, so you can do it while away.
7. **Booking Slots Checking and Selection**: 
   - The script accesses the booking table and waits until 00:00.
   - Upon refreshing the page at 00:00, it scans for available booking slots, ranging from 21:00 to 12:00.
   - It selects the latest available booking slot for you.

<br>

### Assumptions

The email receiving only works with outlook right now.
