from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")

text_input = driver.find_element(By.CSS_SELECTOR, "input#newButtonName.form-control")
text_input.send_keys("SkyPro")

button = driver.find_element(By.CSS_SELECTOR, "button#updatingButton.btn.btn-primary").click()
element = WebDriverWait(driver,20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "button#updatingButton.btn.btn-primary"))
)

blue = element.text
print(blue)