from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")
number_input = driver.find_element(By.XPATH,'//input[@type="number"]')
number_input.send_keys("100", Keys.RETURN)
sleep(5)
number_input.clear()
number_input.send_keys("200", Keys.RETURN)
sleep(5)
driver.quit()