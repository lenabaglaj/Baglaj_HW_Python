from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class CalcPage:
    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def open(self):
        self.driver.get(self.url)

    def do_calc(self):
        text_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        text_input.clear()
        text_input.send_keys("45")

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def perform_element(self):
        self.driver.find_element(By.XPATH, '//span[text()="7"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="+"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="8"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="="]').click()

    def wait_for_result(self):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".screen")))
        self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

    def get_result(self):
        result = self.driver.find_element(By.CSS_SELECTOR, ".screen")
        return result.text