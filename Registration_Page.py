import sys
import json
import time
import random
import string
from xpath import *
from selenium import webdriver
from pdb import set_trace
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


# Manage/install drivers for chrome browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Credentials Used in Testing
FIRST_NAME = 'Taylor'
LAST_NAME = 'Doe'
PHONE_NUMBER = '+610 40000000000'
EMAIL_ADDRESS = 'TaylorDoe@example.com'
PASSWORD = '123@Test'
CONFIRM_PASSWORD = '123@test'

FULL_NAME = 'John Doeee'
EMAIL = 'Johndoeee@mailinator.com'
INVALID_PASSWORD = '123'
VALID_PASSWORD = 'Test@123'


# Function to locate element with wait time and locate/click on the element
def find_html_element(xpath, wait_time=None, click=False):

    try:
        if wait_time:
            element = WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        else:
            element = driver.find_element(By.XPATH, xpath)

        if click:
            element.click()

        return element

    except Exception as e:
        driver.quit()
        return None

# Function for graceful exit from the program with an error message
def find_and_check_element(xpath, wait_time=None, click=False, element_name=None):
    element = find_html_element(xpath, wait_time, click)
    if element is None and element_name:
        print(f"Error: {element_name} not found!!!.")
        sys.exit(1)
    return element


# Function to handle OfficeWorks registration page
def officeworks_createaccount_page():
    attempts = 0
    max_attempts = 2
    
    while attempts < max_attempts:
        try:
            # Visit the Officeworks Create Account Web-Page
            driver.get(OFFICE_WORKS_CREATE_ACCOUNT_PAGE_URL)
            print('Navigate to OfficeWorks Create Account Web-page : SUCCESS')
            break 
        except Exception as e:
            attempts += 1
            print(f'Attempt {attempts}: Error occurred while navigating to the webpage: {e}')
            time.sleep(2)  # Wait for 2 seconds before retrying
    
    if attempts == max_attempts:
        print('Error: Unable to navigate to Office Works Web-page after multiple attempts!')


    # Resize the screen to 1500x1100
    driver.set_window_size(1500, 1100)
   
    try:   
        first_name = find_and_check_element(FIRST_NAME_FIELD_XPATH, 30, click=True, element_name="First Name Field")
        first_name.send_keys(FIRST_NAME)
        print('Input First Name : SUCCESS', '>', FIRST_NAME)
    
        last_name = find_and_check_element(LAST_NAME_FIELD_XPATH, 30, click=True, element_name="Last Name Field")
        last_name.send_keys(LAST_NAME)
        print('Input Last Name : SUCCESS', '>', LAST_NAME)
    
        phone_number = find_and_check_element(PHONE_NUMBER_FIELD_XPATH, 30, click=False, element_name="Phone Number Field")
        phone_number.send_keys(PHONE_NUMBER)
        print('Input Phone Number : SUCCESS', '>', PHONE_NUMBER)
    
        email_address = find_and_check_element(EMAIL_ADDRESS_FIELD_XPATH, 30, click=False, element_name="Email Address Field")
        email_address.send_keys(EMAIL_ADDRESS)
        print('Input Email Address : SUCCESS', '>', EMAIL_ADDRESS)
    
        password = find_and_check_element(PASSWORD_FIELD_XPATH, 30, click=False, element_name="Password Field")
        password.send_keys(PASSWORD)
        print('Input Password : SUCCESS', '>', PASSWORD)
    
        confirm_password = find_and_check_element(CONFIRM_PASSWORD_FIELD_XPATH, 30, click=False, element_name="Confirm Password Field")
        confirm_password.send_keys(CONFIRM_PASSWORD)
        print('Input Confirm Password : SUCCESS', '>', CONFIRM_PASSWORD)
    
        find_and_check_element(CREATE_ACCOUNT_BUTTON_XPATH, 30, click=True, element_name="Create Account Button")
        print('Click on the Create Account Button : SUCCESS')
    
        # Take a screenshot of the Page using Selenium ScreenShot API
        try:
            driver.save_screenshot('officeworks_createaccount_page.png')
            print('ScreenShot Captured Successfully using Selenium ScreenShot API')
            print("Test Scenario 1 : OfficeWorks Create Account, Attempt with Confirm Password Fail Case : SUCCESS")
            print('-------------------------------------------------------------------------------------------------')
        except:
            print('Error : Unable to Capture ScreenShot!')
    
    except:
        print('Error : Unable to Find the Create Account Form Action!!!')


# Test Scenario : 2, Handle Alternative Website's Registration Page
# Function to handle Programiz Registration page
def programiz_signup_page():
    attempts = 0
    max_attempts = 2
    
    while attempts < max_attempts:
        try:
            # Visit the Programiz Sign-up Web-page
            driver.get(PROGRAMIZ_SIGNUP_PAGE_URL)
            print('Navigate to Programiz Sign-up Web-page : SUCCESS')

            break 
        except Exception as e:
            attempts += 1
            print(f'Attempt {attempts}: Error occurred while navigating to the webpage: {e}')
            time.sleep(2)  # Wait for 2 seconds before retrying
    
    if attempts == max_attempts:
        print('Error: Unable to navigate to Programiz Sign-up Web-page after multiple attempts!')

    try:   

        find_and_check_element(SIGNUP_WITH_EMAIL_BUTTON_XPATH, 30, click=True, element_name="Sign-up with Email Button")
        print('Click on the Sign-up with Email Button : SUCCESS')

        full_name = find_and_check_element(FULL_NAME_FIELD_XPATH, 40, click=True, element_name=" Programiz Full Name Field")
        full_name.clear()
        full_name.send_keys(FULL_NAME)
        time.sleep(2)
        print('Input First Name : SUCCESS', '>', FULL_NAME)
    
    
        email = find_and_check_element(EMAIL_FIELD_XPATH, 30, click=False, element_name="Programiz Email Field")
        email.send_keys(EMAIL)
        print('Input Email Address : SUCCESS', '>', EMAIL)
    
        # Attempt with Invalid Password : FAIL CASE
        udemypassword = find_and_check_element(PROGRAMIZ_PASSWORD_FIELD_XPATH, 30, click=False, element_name="Programiz Password Field")
        udemypassword.send_keys(INVALID_PASSWORD)
        print('Input Invalid Password : SUCCESS', '>', INVALID_PASSWORD)
    
        find_and_check_element(SIGNUP_BUTTON_XPATH, 30, click=True, element_name="Programiz Sign-up Button")
        print('Click on the Sign-up Button : SUCCESS')
        time.sleep(6)

        # Take a screenshot of the page
        try:
            driver.save_screenshot('PROGRAMIZ_signup_failed.png')
            print('ScreenShot Captured Successfully using Selenium ScreenShot API')
            print("Test Scenario 2 : Alternative Web-page registration page, Attempt Failing Sign-up Case : SUCCESS")
        except:
            print('Error : Unable to Capture ScreenShot!')

        # Attempt with Valid Password : SUCCESS CASE    
        password = find_and_check_element(PROGRAMIZ_PASSWORD_FIELD_XPATH, 30, click=False, element_name="Programiz Password Field")
        password.send_keys(VALID_PASSWORD)
        print('Input Valid Password : SUCCESS', VALID_PASSWORD)

        find_and_check_element(SIGNUP_BUTTON_XPATH, 30, click=True, element_name="Programiz Sign-up Button")
        print('Click on the Sign-up Button : SUCCESS')
        time.sleep(5)
    
        # Take a screenshot of the page
        try:
            driver.save_screenshot('Programiz_signup_success.png')
            print('ScreenShot Captured Successfully using Seleniun ScreenShot API')
            print("Test Scenario 2 : Alternative Web-page registration page, Attempt Passing Sign-up Case : SUCCESS")
        except:
            print('Error : Unable to Capture ScreenShot!')
    
    except:
        print('Error : Unable to Find the Sign-up Form Action!!!')



officeworks_createaccount_page()
programiz_signup_page()        
        
time.sleep(3)
driver.quit()














