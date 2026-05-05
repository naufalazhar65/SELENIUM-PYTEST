from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from time import sleep

BASE_URL = ("https://ecommerce-playground.lambdatest.io/index.php?route=account/register")

FIRST_NAME = ("Naufal")
LAST_NAME = ("Azhar")
EMAIL = ("naufalazhar858@gmail.com")
TELP = ("08161363")
PASSWORD = ("123456")
CONFIRM_PASSWORD = ("123456")

def test_valid_registration(driver):
    # Test for a valid registration

    driver.get(BASE_URL)

    assert 'Register Account' in driver.title

    # Fill in registration form
    input_firstName = driver.find_element(By.ID, "input-firstname")
    input_lastName = driver.find_element(By.ID, "input-lastname")
    input_email = driver.find_element(By.ID, "input-email")
    input_telp = driver.find_element(By.ID, "input-telephone")
    input_password = driver.find_element(By.ID, "input-password")
    input_confirm_password = driver.find_element(By.ID, "input-confirm")

    input_firstName.send_keys(FIRST_NAME)
    input_lastName.send_keys(LAST_NAME)
    input_email.send_keys(EMAIL)
    input_telp.send_keys(TELP)
    input_password.send_keys(PASSWORD)
    input_confirm_password.send_keys(CONFIRM_PASSWORD)

    # Select options
    label = driver.find_element(By.XPATH, "//label[normalize-space()='Yes']")
    label.click()

    radio = driver.find_element(By.XPATH, "//input[@name='newsletter' and @value='1']")
    if radio.is_selected():
        print("Radio is selected.")
    else:
        print("Radiio is NOT selected.")
    assert radio.is_selected()

    label_agree = driver.find_element(By.XPATH, "//label[@for='input-agree']")
    label_agree.click()

    check_agree = driver.find_element(By.XPATH, "//input[@name='agree' and @value='1']")
    if check_agree.is_selected():
        print("Checkbox is selected.")
    else:
        print("Checkbox is NOT selected.")
    assert check_agree.is_selected()

    # Continue with registration
    continue_btn = driver.find_element(By.XPATH, '//body/div[1]/div[5]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/input[1]')
    continue_btn.click()

    sleep(3)

    # Verify success message
    success_msg = "Your Account Has Been Created!"
    assert success_msg in driver.find_element(By.TAG_NAME, 'h1').text

def test_existing_email_registration(driver):
    # Test for an existing email registration

    driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/register")

    assert 'Register Account' in driver.title

    # Fill in registration form with existing email
    input_firstName = driver.find_element(By.ID, "input-firstname")
    input_lastName = driver.find_element(By.ID, "input-lastname")
    input_email = driver.find_element(By.ID, "input-email")
    input_telp = driver.find_element(By.ID, "input-telephone")
    input_password = driver.find_element(By.ID, "input-password")
    input_confirm_password = driver.find_element(By.ID, "input-confirm")

    input_firstName.send_keys(FIRST_NAME)
    input_lastName.send_keys(LAST_NAME)
    input_email.send_keys(EMAIL)
    input_telp.send_keys(TELP)
    input_password.send_keys(PASSWORD)
    input_confirm_password.send_keys(CONFIRM_PASSWORD)

    # Select options

    label = driver.find_element(By.XPATH, "//label[normalize-space()='Yes']")
    label.click()

    radio = driver.find_element(By.XPATH, "//input[@name='newsletter' and @value='1']")
    if radio.is_selected():
        print("Radio is selected.")
    else:
        print("Radiio is NOT selected.")
    assert radio.is_selected()

    label_agree = driver.find_element(By.XPATH, "//label[@for='input-agree']")
    label_agree.click()

    check_agree = driver.find_element(By.XPATH, "//input[@name='agree' and @value='1']")
    if check_agree.is_selected():
        print("Checkbox is selected.")
    else:
        print("Checkbox is NOT selected.")
    assert check_agree.is_selected()

    # Continue with registration
    continue_btn = driver.find_element(By.XPATH, '//body/div[1]/div[5]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/input[1]')
    continue_btn.click()

    sleep(3)

    # Verify error message for existing email
    error_msg = "Warning: E-Mail Address is already registered!"
    assert error_msg in driver.find_element(By.XPATH, '//body/div[1]/div[5]/div[1]/div[1]').text

def test_mismatched_passwords_registration(driver):
    # Test for mismatched passwords during registration

    driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/register")

    assert 'Register Account' in driver.title

    # Fill in registration form with mismatched passwords
    input_firstName = driver.find_element(By.ID, "input-firstname")
    input_lastName = driver.find_element(By.ID, "input-lastname")
    input_email = driver.find_element(By.ID, "input-email")
    input_telp = driver.find_element(By.ID, "input-telephone")
    input_password = driver.find_element(By.ID, "input-password")
    input_confirm_password = driver.find_element(By.ID, "input-confirm")

    input_firstName.send_keys("name1")
    input_lastName.send_keys("name2")
    input_email.send_keys("naufal2@gmail.com")
    input_telp.send_keys("873627572")
    input_password.send_keys("password123")
    input_confirm_password.send_keys("password134")

    # Select options
    label = driver.find_element(By.XPATH, "//label[normalize-space()='Yes']")
    label.click()

    radio = driver.find_element(By.XPATH, "//input[@name='newsletter' and @value='1']")
    if radio.is_selected():
        print("Radio is selected.")
    else:
        print("Radiio is NOT selected.")
    assert radio.is_selected()

    label_agree = driver.find_element(By.XPATH, "//label[@for='input-agree']")
    label_agree.click()

    check_agree = driver.find_element(By.XPATH, "//input[@name='agree' and @value='1']")
    if check_agree.is_selected():
        print("Checkbox is selected.")
    else:
        print("Checkbox is NOT selected.")
    assert check_agree.is_selected()

    # Continue with registration
    continue_btn = driver.find_element(By.XPATH, '//body/div[1]/div[5]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/input[1]')
    continue_btn.click()

    sleep(3)

    # Verify error message for mismatched passwords
    error_msg = "Password confirmation does not match password!"
    assert error_msg in driver.find_element(By.XPATH, "//div[contains(text(),'Password confirmation does not match password!')]").text
