from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def made_cart(self):
        text_input = self.driver.find_element(By.CSS_SELECTOR, "input#first-name")
        text_input.send_keys("Елена")

        text_input = self.driver.find_element(By.CSS_SELECTOR, "input#last-name")
        text_input.send_keys("Баглай")

        text_input = self.driver.find_element(By.CSS_SELECTOR, "input#postal-code")
        text_input.send_keys("602267")

        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()

    def get_total_amount(self):
        try:
            total_cost = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
            ).text
            total_cost_value = float(total_cost.split("$")[1])
            return total_cost_value
        except Exception as e:
            print(f"An error occurred while retrieving the total amount: {e}")
            return None