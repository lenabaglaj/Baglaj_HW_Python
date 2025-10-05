from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

class IntPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def do_int(self):
        text_input = self.driver.find_element(By.CSS_SELECTOR, "input#user-name")
        text_input.send_keys("standard_user")
        text_input = self.driver.find_element(By.CSS_SELECTOR, "input#password")
        text_input.send_keys("secret_sauce")
        self.driver.find_element(By.CSS_SELECTOR, "input#login-button").click()