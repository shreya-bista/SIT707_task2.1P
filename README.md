## Selenium Web Automation: Registration Form Testing
This project demonstrates how to use Selenium WebDriver with Python to automate the testing of registration forms on two different websites: Officeworks and Programiz.

## Install required packages
pip install -r requirements.txt

## Start Test
python Registration_Page.py

## Requirements
1. Python 3.x
2. Selenium
3. webdriver_manager
4. Google Chrome 

### Prerequisites
Before running the script, ensure you have the following:

- Python 3.x installed: [Download Python](https://www.python.org/downloads/)
- Chrome browser installed: [Download Chrome](https://www.google.com/chrome/)
- ChromeDriver executable: [Download ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
- Note: Make sure to download the ChromeDriver version compatible with your installed Chrome browser.

### How To Run

1. Clone this repository

2. Open a terminal or command prompt and navigate to the project directory.

3. Run the script: 
python Registration_Page.py

4. The script will launch a Chrome browser and start test. You will see the output messages indicating the progress and success of each step.

5. After completing the execution, the script will exit, and the Chrome browser will close automatically.

## Script Overview
The code automates the following scenarios:

1. Officeworks Registration Form:
- Navigate to the Officeworks Create Account webpage
- Fill in the registration form with provided personal information
- Intentionally fail the password confirmation requirement
- Submit the form
- Capture a screenshot of the page with error messages

2. Programiz Registration Form:
- Navigate to the Programiz Signup webpage
- Click the "Sign up with Email" button
- Fill in the registration form with invalid password (fail case)
- Submit the form
- Capture a screenshot of the page with error messages
- Fill in the registration form with valid password (success case)
- Submit the form
- Capture a screenshot of the page after successful registration

## Output
The script will generate the following screenshot files in the project directory:

1. officeworks_createaccount_page.png: Screenshot of the Officeworks registration page with the failed password confirmation.
2. PROGRAMIZ_signup_failed.png: Screenshot of the Programiz registration page with the failed invalid password attempt.
3. Programiz_signup_success.png: Screenshot of the Programiz registration page after successful registration with a valid password.
