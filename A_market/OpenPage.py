from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class OpenPage:
    url = "https://market-place-next-mu.vercel.app"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def open(self):
        self.driver.get(self.url)

    def do_write(self):
        text_input = self.driver.find_element((By.XPATH, "//input[@class='HeaderForm_form_search_4iesf']"))
        text_input.clear()
        text_input.send_keys("Мыло")
        text_input.send_keys(Keys.RETURN)