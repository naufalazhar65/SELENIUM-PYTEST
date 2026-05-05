from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

BASE_URL = ("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")
EMAIL = ("naufalazhar65@gmail.com")
PASSWORD = ("naufal354")

def test_valid_login(driver):
    driver.get(BASE_URL)
    
    assert 'Account Login' in driver.title

    input_email = driver.find_element(By.ID, "input-email")
    input_email.send_keys(EMAIL)

    input_password = driver.find_element(By.ID, "input-password")
    input_password.send_keys(PASSWORD)

    print(f"Email input value is: {input_email.get_attribute('value')}")
    assert input_email.get_attribute('value') == "naufalazhar65@gmail.com"

    print(f"Password input value is: {input_password.get_attribute('value')}")
    assert input_password.get_attribute('value') == "naufal354"

    login_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[1]/div/div/div/div[2]/div/div/form/input')
    login_button.click()
    sleep(2)
    WebDriverWait(driver, 10).until(
        EC.title_contains("My Account")
    )
    # Assertion: Verify successful login
    # assert 'My Account' in driver.title
    # verify_login_success = driver.find_element(By.TAG_NAME, 'h2')
    # assert verify_login_success.text == 'My Account'

def test_invalid_login(driver):
    driver.get(BASE_URL)
    # driver.maximize_window()

    assert 'Account Login' in driver.title

    # Input invalid email and password
    input_email = driver.find_element(By.ID, "input-email")
    input_password = driver.find_element(By.ID, "input-password")
    input_email.send_keys("invalid_email@gmail.com")
    input_password.send_keys("invalid_password")

    login_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[1]/div/div/div/div[2]/div/div/form/input')
    login_button.click()
    sleep(2)

    # Assertion: Verify error message
    error_message = driver.find_element(By.XPATH, '//div[contains(@class, "alert-danger")]')
    
    if error_message.is_displayed():
        expected_texts = [
            'Warning: No match for E-Mail Address and/or Password.',
            'Warning: Your account has exceeded allowed number of login attempts. Please try again in 1 hour.'
        ]
        assert error_message.text in expected_texts, f"Unexpected error message displayed: {error_message.text}"
    else:
        raise AssertionError("Error message not displayed.")


