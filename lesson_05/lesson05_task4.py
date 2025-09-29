from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/login")

username_input = driver.find_element(By.XPATH,'//input[@id="username"]')
username_input.send_keys("tomsmith")

password_input = driver.find_element(By.XPATH,'//input[@id="password"]')
password_input.send_keys("SuperSecretPassword!")

button = driver.find_element(By.CSS_SELECTOR, "button.radius")
button.click()

banner = driver.find_element(By.XPATH,'//div[@id="flash"]')
text_content = banner.text

print("Извлеченный текст:", text_content)