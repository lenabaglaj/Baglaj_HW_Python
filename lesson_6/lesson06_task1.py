from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/ajax")

element = WebDriverWait(driver,30).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '#ajaxButton'))
)

button = driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()
element = WebDriverWait(driver,30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'p.bg-success'))
)

green = element.text
print(green)

driver.quit()