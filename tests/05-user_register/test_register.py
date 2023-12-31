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

def test_valid_registration(driver):
    # Test for a valid registration

    driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/register")

    assert 'Register Account' in driver.title

    # Fill in registration form
    input_firstName = driver.find_element(By.ID, "input-firstname")
    input_lastName = driver.find_element(By.ID, "input-lastname")
    input_email = driver.find_element(By.ID, "input-email")
    input_telp = driver.find_element(By.ID, "input-telephone")
    input_password = driver.find_element(By.ID, "input-password")
    input_confirm_password = driver.find_element(By.ID, "input-confirm")

    input_firstName.send_keys("Naufal")
    input_lastName.send_keys("Azhar")
    input_email.send_keys("naufal5@gmail.com")
    input_telp.send_keys("012332532")
    input_password.send_keys("naufal354")
    input_confirm_password.send_keys("naufal354")

    # Select options
    rd_btn = driver.find_element(By.XPATH, "//label[contains(text(),'Yes')]")
    rd_btn.click()
    rd_btn.is_selected(), "Select Yes"

    check_btn = driver.find_element(By.XPATH, "//body/div[1]/div[5]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/label[1]")
    check_btn.click()
    check_btn.is_selected(), "Check Agree"

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

    input_firstName.send_keys("name1")
    input_lastName.send_keys("name2")
    input_email.send_keys("naufal2@gmail.com")
    input_telp.send_keys("873627572")
    input_password.send_keys("password123")
    input_confirm_password.send_keys("password123")

    # Select options
    rd_btn = driver.find_element(By.XPATH, "//label[contains(text(),'Yes')]")
    rd_btn.click()
    print("Select Yes", rd_btn.is_selected())

    check_btn = driver.find_element(By.XPATH, "//body/div[1]/div[5]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/label[1]")
    check_btn.click()
    print("Check Agree", check_btn.is_selected())

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
    input_confirm_password.send_keys("password134   ")

    # Select options
    rd_btn = driver.find_element(By.XPATH, "//label[contains(text(),'Yes')]")
    rd_btn.click()
    print("Select Yes", rd_btn.is_selected())

    check_btn = driver.find_element(By.XPATH, "//body/div[1]/div[5]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/label[1]")
    check_btn.click()
    print("Check Agree", check_btn.is_selected())

    # Continue with registration
    continue_btn = driver.find_element(By.XPATH, '//body/div[1]/div[5]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/input[1]')
    continue_btn.click()

    sleep(3)

    # Verify error message for mismatched passwords
    error_msg = "Password confirmation does not match password!"
    assert error_msg in driver.find_element(By.XPATH, "//div[contains(text(),'Password confirmation does not match password!')]").text
