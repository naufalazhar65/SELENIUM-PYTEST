import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
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

def test_checkout(driver):
    driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")

    assert 'Account Login' in driver.title

    # Login
    input_email = driver.find_element(By.ID, "input-email")
    input_password = driver.find_element(By.ID, "input-password")

    input_email.send_keys("naufalazhar65@gmail.com")
    input_password.send_keys("naufal354")

    login_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[1]/div/div/div/div[2]/div/div/form/input')
    login_button.click()
    sleep(2)

    assert 'My Account' in driver.title
    verify_login_success = driver.find_element(By.TAG_NAME, 'h2')
    assert verify_login_success.text == 'My Account'

    # Navigate to Cart
    cart_button = driver.find_element(By.XPATH, "//header/div[@id='main-header']/div[@id='entry_217820']/div[@id='entry_217825']/a[1]/div[1]")
    cart_button.click()
    sleep(2)

    # Proceed to Checkout
    checkout_button = driver.find_element(By.XPATH, '//body/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/a[1]')
    checkout_button.click()
    sleep(2)

    assert 'Checkout' in driver.title

    # Verify Cart Items
    verify_cart_card = driver.find_element(By.XPATH, '//body/div[1]/div[5]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[1]')
    assert verify_cart_card.is_displayed()

    # Verify Product List
    verify_product_list_1 = driver.find_element(By.XPATH, '//body[1]/div[1]/div[5]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/a[1]')
    assert verify_product_list_1.text == 'HTC Touch HD'
    verify_product_list_2 = driver.find_element(By.XPATH, '//body[1]/div[1]/div[5]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/a[1]')
    assert verify_product_list_2.text == 'iMac'

    check_btn = driver.find_element(By.XPATH, "//body/div[1]/div[5]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[5]/label[1]")
    check_btn.click()

    continue_btn = driver.find_element(By.XPATH, "//button[@id='button-save']")
    continue_btn.click()
    sleep(3)

    ### VERIFY USER IS NAVIGATED TO CONFIRM ORDER PAGE ###

    assert driver.current_url == "https://ecommerce-playground.lambdatest.io/index.php?route=extension/maza/checkout/confirm"
    get_title = "Confirm Order"
    assert get_title in driver.title
    assert "Confirm Order" in driver.page_source
    assert "Payment Address" in driver.page_source
    assert "Shipping Address" in driver.page_source
    assert "Shipping Method:" in driver.page_source

    product_information = driver.find_element(By.CLASS_NAME, 'table-bordered')
    assert product_information.is_displayed()
    assert "HTC Touch HD" in product_information.text
    assert "iMac" in product_information.text

    tbody = driver.find_element(By.XPATH, '//table/tbody')
    rows_at_index_2 = tbody.find_elements(By.XPATH, './tr')
    expected_length = 2
    assert len(rows_at_index_2) == expected_length, f"Expected length: {expected_length}, Actual length: {len(rows_at_index_2)}"

    # Payment Address
    card_bodies = driver.find_elements(By.CLASS_NAME, 'card-body')
    expected_text = 'Naufal Azhar\nPt.mamkmur\njalan1\njalan2\njakarta 1234\nJawa Barat,Indonesia'
    actual_text = card_bodies[0].text
    assert expected_text == actual_text, f"Expected: {expected_text}, Actual: {actual_text}"

    # Shipping Address
    expected_text = 'Naufal Azhar\nPt.mamkmur\njalan1\njalan2\njakarta 1234\nJawa Barat,Indonesia'
    actual_text = card_bodies[1].text
    assert expected_text == actual_text, f"Expected: {expected_text}, Actual: {actual_text}"

    # Shipping Method
    expected_text = 'Flat Shipping Rate'
    actual_text = card_bodies[2].text
    assert expected_text == actual_text, f"Expected: {expected_text}, Actual: {actual_text}"

    confirm_btn = driver.find_element(By.XPATH, "//button[@id='button-confirm']")
    confirm_btn.click()
    sleep(3)

    assert driver.current_url == "https://ecommerce-playground.lambdatest.io/index.php?route=checkout/success"
    assert "Your order has been placed!" in driver.title

    success_msg = "Your order has been placed!"
    assert success_msg in driver.find_element(By.TAG_NAME, "h1").text
    assert "Your order has been successfully processed!" in driver.page_source
    sleep(5)