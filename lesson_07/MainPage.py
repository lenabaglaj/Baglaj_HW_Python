from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, product_selector):
        product_button = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, product_selector))
        )
        product_button.click()

    def get_shop(self):
        self.driver.find_element(By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-onesie").click()
        self.driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()
        self.driver.find_element(By.CSS_SELECTOR, "button#checkout").click()
        sleep(10)