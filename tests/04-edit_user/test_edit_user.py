from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

BASE_URL = ("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")
EMAIL = ("naufalazhar65@gmail.com")
PASSWORD = ("naufal354")

FIRST_NAME = ("Naufal")
LAST_NAME = ("Azhar")
EDIT_MAIL = ("naufalazhar65@gmail.com")
INPUT_TELP = ("08127836")



def test_edit_user(driver):
    # Navigate to the login page
    driver.get(BASE_URL)

    # Check if the correct page is loaded
    assert 'Account Login' in driver.title

    # Input valid email and password
    input_email = driver.find_element(By.ID, "input-email")
    input_password = driver.find_element(By.ID, "input-password")
    input_email.send_keys(EMAIL)
    input_password.send_keys(PASSWORD)

    # Click the login button
    login_button = driver.find_element(By.XPATH, '//input[@value="Login"]')
    login_button.click()
    sleep(2)

    # Navigate to the edit account page
    driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/edit")
    assert 'My Account Information' in driver.title

    # Edit user details
    input_firstName = driver.find_element(By.ID, 'input-firstname')
    input_lastName = driver.find_element(By.ID, 'input-lastname')
    input_editEmail = driver.find_element(By.ID, 'input-email')
    input_telp = driver.find_element(By.ID, 'input-telephone')

    input_firstName.clear()
    input_firstName.send_keys(FIRST_NAME)
    input_lastName.clear()
    input_lastName.send_keys(LAST_NAME)
    input_editEmail.clear()
    input_editEmail.send_keys(EDIT_MAIL)
    input_telp.clear()
    input_telp.send_keys(INPUT_TELP)

    # Click the continue button
    continue_button = driver.find_element(By.XPATH, '//input[@value="Continue"]')
    continue_button.click()
    sleep(2)

    # Verify success message
    success_message = "Success: Your account has been successfully updated."
    assert success_message in driver.find_element(By.XPATH, '//body/div[1]/div[5]/div[1]/div[1]').text
    sleep(2)

    # Verify user details have been edited
    driver.find_element(By.LINK_TEXT, 'Edit Account').click()
    verify = driver.find_element(By.ID, 'input-telephone')
    print(f"Input telp: {verify.get_attribute('value')}")

    assert verify.get_attribute('value') == INPUT_TELP

    sleep(5)
