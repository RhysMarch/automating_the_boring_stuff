# Court Booking Automation
This is a personal project and isn't intended to be used by people other than me. 

This script automates volleyball court bookings released at midnight. 
It requires Microsoft Authenticator for login, necessitating human intervention. 
The rest of the process is automated.

The script only works when I authenticate the 2FA login. This ensures fairness as I'm actively involved in the process and not automating bookings while away. 
Also, the script doesn't impact my booking success, as I'd achieve the same results manually.
<br> If 2FA wasn't needed, it would be completely automated.

## How it works

1. You install the requirements in requirements.txt.
2. You enter your login details in the config.json file.
3. You run the python file. 
4. The script will keep checking until it is 23:59. 
5. Once 23:59, the automation process begins. 
6. The script opens the booking URL, logs you in with the provided email and password in the config.json file. 
7. You authenticate the login with microsoft authenticator. 
8. You are directed to the volleyball booking table and the script checks the available bookings, from 21:00 to 12:00. Picking the latest booking possible.