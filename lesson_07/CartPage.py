from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def shop_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()
        self.driver.find_element(By.CSS_SELECTOR, "button#checkout").click()