import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from time import sleep

@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    # options.add_argument('--headless')
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(15)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_edit_user(driver):
    # Navigate to the login page
    driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")

    # Check if the correct page is loaded
    assert 'Account Login' in driver.title

    # Input valid email and password
    input_email = driver.find_element(By.ID, "input-email")
    input_password = driver.find_element(By.ID, "input-password")
    input_email.send_keys("naufalazhar65@gmail.com")
    input_password.send_keys("naufal354")

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
    input_firstName.send_keys('Naufal')
    input_lastName.clear()
    input_lastName.send_keys('Azhar')
    input_editEmail.clear()
    input_editEmail.send_keys('naufalazhar65@gmail.com')
    input_telp.clear()
    input_telp.send_keys('9876543')

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
    assert verify.get_attribute('value') == '9876543'

    sleep(5)
