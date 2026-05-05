import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = "https://ecommerce-playground.lambdatest.io/index.php?route=account/login"

EMAIL = os.getenv("naufalazhar65@gmail.com")
PASSWORD = os.getenv("naufal354")


def test_valid_login(driver):
    driver.get(BASE_URL)

    assert "Account Login" in driver.title

    # Input field
    email_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "input-email"))
    )
    password_input = driver.find_element(By.ID, "input-password")

    email_input.send_keys(EMAIL)
    password_input.send_keys(PASSWORD)

    # Login button (lebih stabil)
    login_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[1]/div/div/div/div[2]/div/div/form/input')
    login_button.click()

    # Wait sampai login sukses
    WebDriverWait(driver, 10).until(
        EC.title_contains("My Account")
    )

    assert "My Account" in driver.title

    heading = driver.find_element(By.TAG_NAME, "h2")
    assert heading.text == "My Account"


# def test_invalid_login(driver):
#     driver.get(BASE_URL)

#     assert "Account Login" in driver.title

#     driver.find_element(By.ID, "input-email").send_keys("invalid@email.com")
#     driver.find_element(By.ID, "input-password").send_keys("wrongpassword")

#     login_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[1]/div/div/div/div[2]/div/div/form/input')
#     login_button.click()

#     # Wait error muncul
#     error = WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger"))
#     )

#     expected_texts = [
#         "Warning: No match for E-Mail Address and/or Password.",
#         "Warning: Your account has exceeded allowed number of login attempts. Please try again in 1 hour."
#     ]

#     assert error.text in expected_texts