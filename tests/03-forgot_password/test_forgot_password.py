from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def test_forgot_password(driver):
    driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")

    driver.find_element(By.LINK_TEXT, 'Forgotten Password').click()
    assert driver.current_url == "https://ecommerce-playground.lambdatest.io/index.php?route=account/forgotten"
    assert 'Forgot Your Password?' in driver.title
    assert 'Forgot Your Password?' in driver.page_source

    input_email = driver.find_element(By.ID, 'input-email')
    input_email.send_keys('naufalazhar65@gmail.com')

    continue_button = driver.find_element(By.XPATH, "//button[contains(text(),'Continue')]")
    continue_button.click()
    sleep(2)
    success_message = 'An email with a confirmation link has been sent your email address.'
    assert success_message in driver.find_element(By.XPATH, '//body/div[1]/div[5]/div[1]/div[1]').text
