import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from time import sleep

@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--headless')
    
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(15)
    driver.maximize_window()
    
    yield driver
    driver.quit()

def test_change_user_password(driver):
    # Login
    driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")
    input_email = driver.find_element(By.ID, "input-email")
    input_password = driver.find_element(By.ID, "input-password")

    input_email.send_keys("naufal5@gmail.com")
    input_password.send_keys("naufal13")

    login_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[1]/div/div/div/div[2]/div/div/form/input')
    login_button.click()
    sleep(2)

    # Navigate to change password page
    driver.find_element(By.LINK_TEXT, 'Password').click()

    # Verify navigation
    assert 'Change Password' in driver.title
    assert driver.current_url == 'https://ecommerce-playground.lambdatest.io/index.php?route=account/password'

    # Enter new password
    new_password = driver.find_element(By.ID, 'input-password')
    confirm_password = driver.find_element(By.ID, 'input-confirm')
    new_password.send_keys('naufal14')
    confirm_password.send_keys('naufal14')

    # Verify entered passwords
    assert new_password.get_attribute('value') == 'naufal14'
    assert confirm_password.get_attribute('value') == 'naufal14'

    # Submit new password
    continue_btn = driver.find_element(By.XPATH, "//input[@type='submit']")
    continue_btn.click()

    sleep(3)

    # Verify success message
    success_msg = 'Success: Your password has been successfully updated.'
    assert success_msg in driver.find_element(By.CLASS_NAME, 'alert-success').text

def test_login_with_new_password(driver):
    # Login with new password
    driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")
    input_email = driver.find_element(By.ID, "input-email")
    input_password = driver.find_element(By.ID, "input-password")

    input_email.send_keys("naufal5@gmail.com")
    input_password.send_keys("naufal14")

    login_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[1]/div/div/div/div[2]/div/div/form/input')
    login_button.click()
    sleep(2)

    # Verify successful login
    assert 'My Account' in driver.title
    verify_login_success = driver.find_element(By.TAG_NAME, 'h2')
    assert verify_login_success.text == 'My Account'
