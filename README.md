# Court Booking Automation
This is a personal project and isn't intended to be used by people other than me. 

This script automates volleyball court bookings released at midnight. 
It requires Microsoft Authenticator for login, necessitating human intervention. 
The rest of the process is automated.

The script only works when I authenticate the 2FA login. This ensures fairness as I'm actively involved in the process and not automating bookings while away. 
Also, the script doesn't impact my booking success, as I'd achieve the same results manually.

## Config.json Settings 

- `email`: This is the email address used for logging into the NCL booking system. It's the username part of your credentials for accessing the booking platform.

- `password`: This is the password associated with your email for the NCL booking system.

- `sender-email`: This is the email address used to send notifications. It's the "From" address in the emails that the script sends. 

- `recipient-email`: This is the email address where you want to receive notifications. It's the "To" address in the emails. This could be the same as `sender-email` if you're sending notifications to yourself.


## How it works

1. You install the requirements in requirements.txt.
2. You enter your details in the config.json file.
3. You run the python file. 
4. The script will keep checking until it is 23:55. 
5. Once 23:55, the automation process begins. 
6. The script opens the booking URL, logs you in with the provided email and password in the config.json file. 
7. You authenticate the login with microsoft authenticator. 
8. You are directed to the volleyball booking table and the script checks the available bookings, from 21:00 to 12:00. Picking the latest booking possible.

<br>

### Assumptions

I believe the email receiving only works with outlook, though I'm not sure.
