from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def test_form():
    browser = webdriver.Edge(service=EdgeService(
    EdgeChromiumDriverManager().install()))
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    text_input = browser.find_element(By.CSS_SELECTOR, '[name="first-name"]')
    text_input.send_keys("Иван")

    text_input = browser.find_element(By.CSS_SELECTOR, '[name="last-name"]')
    text_input.send_keys("Петров")

    text_input = browser.find_element(By.CSS_SELECTOR, '[name="address"]')
    text_input.send_keys("Ленина, 55-3")

    text_input = browser.find_element(By.CSS_SELECTOR, '[name="e-mail"]')
    text_input.send_keys("test@skypro.com")

    text_input = browser.find_element(By.CSS_SELECTOR, '[name="phone"]')
    text_input.send_keys("+7985899998787")

    text_input = browser.find_element(By.CSS_SELECTOR, '[name="city"]')
    text_input.send_keys("Москва")

    text_input = browser.find_element(By.CSS_SELECTOR, '[name="country"]')
    text_input.send_keys("Россия")

    text_input = browser.find_element(By.CSS_SELECTOR, '[name="job-position"]')
    text_input.send_keys("QA")

    text_input = browser.find_element(By.CSS_SELECTOR, '[name="company"]')
    text_input.send_keys("SkyPro")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-outline-primary.mt-3").click()
    browser.execute_script("arguments[0].scrollIntoView();", button)
    browser.execute_script("arguments[0].click();", button)
    element = WebDriverWait(browser,90).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.btn-outline-primary.mt-3"))
)

    pole_z = browser.find_element(By.ID, "zip-code").get_attribute("class")
    assert pole_z == "alert py-2 alert-danger"

    poles = ["#first-name", "#last-name", "#address", "#city", "#country", "#e-mail", "#phone", "#company"]
    for pole in poles:
        pole_class = browser.find_element(By.CSS_SELECTOR, pole).get_attribute("class")
        assert pole_class == "alert py-2 alert-success"

    browser.quit()