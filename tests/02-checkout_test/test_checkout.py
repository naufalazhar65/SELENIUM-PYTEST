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
    options.add_argument('--headless')
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

    sleep(5)




    # element = self.driver.find_element(By.LINK_TEXT, "HTC Touch HD")
    # actions = ActionChains(self.driver)
    # actions.move_to_element(element).perform()
    # element = self.driver.find_element(By.CSS_SELECTOR, "body")
    # actions = ActionChains(self.driver)
    # actions.move_to_element(element, 0, 0).perform()
    # self.driver.find_element(By.LINK_TEXT, "Checkout").click()
    # self.driver.find_element(By.NAME, "address_id").click()
    # self.driver.find_element(By.CSS_SELECTOR, ".custom-control:nth-child(5) > .custom-control-label").click()
    # self.driver.find_element(By.CSS_SELECTOR, ".custom-control:nth-child(5) > .custom-control-label").click()
    # self.driver.find_element(By.ID, "input-comment").click()
    # self.driver.find_element(By.ID, "input-comment").send_keys("hallo")
    # self.driver.find_element(By.CSS_SELECTOR, ".custom-control:nth-child(6) > .custom-control-label").click()
    # self.driver.find_element(By.ID, "button-save").click()
  
