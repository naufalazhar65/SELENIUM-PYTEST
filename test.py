import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains

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

def test_add_product_rating(driver):
    # Navigate to the webpage
    driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=107")

    element_to_scroll = driver.find_element(By.ID, 'rating-4-216860')
    actions = ActionChains(driver)
    actions.move_to_element(element_to_scroll).perform()
    element_to_scroll.click()


    # star = driver.find_element(By.CLASS_NAME, 'start-form-check')
    # input = star.find_elements(By.TAG_NAME, 'input')
    # expected_length = 6
    # assert len(input) == expected_length, f"Expected length: {expected_length}, Actual length: {len(input)}"
    # target_index = 2  # Ganti dengan indeks yang diinginkan
    # input[target_index].click()
    # Wait for the start form check elements to be present
    # start_form_check = WebDriverWait(driver, 10).until(
    #     EC.presence_of_all_elements_located((By.CLASS_NAME, 'start-form-check'))
    # )
    # sleep(2)
    # # Find all input elements within the start form check
    # start_form_check.find_element(By.TAG_NAME, 'input').is_displayed()

    # Check if there are exactly 6 input elements
    # assert len(inputs) == 6, "Expected 6 input elements, but found {}".format(len(inputs))

    # Click on the second input element
    # inputs[1].click()

    # Optionally, you can add a wait here to ensure the click has taken effect
    # For example:
    # WebDriverWait(setup, 5).until(EC.element_to_be_clickable((By.XPATH, 'your_xpath_here')))

    # Assertion to check if the second input element is selected
    # assert inputs[1].is_selected(), "The second input element should be selected"