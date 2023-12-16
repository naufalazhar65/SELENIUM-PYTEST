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

def test_add_product_to_cart(driver):
    # Open the website
    driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=common/home")

    # Select a product
    select_product = driver.find_element(By.XPATH, "//a[@id='mz-product-listing-image-37213259-0-1']")
    select_product.click()

    # Add the product to the cart
    add_cart_btn = driver.find_element(By.XPATH, "//div[@id='entry_216842']")
    assert add_cart_btn.is_displayed()
    add_cart_btn.click()
    sleep(3)

    # Verify success message
    success_msg = "Success: You have added\niMac\nto your\nshopping cart\n!"
    notification_text = driver.find_element(By.XPATH, "//div[@id='notification-box-top']").text
    assert success_msg in notification_text

    # Verify the cart badge number
    verify_cart_badge_num = "1"
    cart_badge_num = driver.find_element(By.CLASS_NAME, 'cart-icon').text
    assert verify_cart_badge_num in cart_badge_num
