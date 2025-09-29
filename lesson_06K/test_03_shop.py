import pytest
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_shop_total_cost():
    driver = webdriver.Firefox(service=FirefoxService(
    GeckoDriverManager().install()))
    driver.get("https://www.saucedemo.com/")

    text_input = driver.find_element(By.CSS_SELECTOR, "input#user-name")
    text_input.send_keys("standard_user")

    text_input = driver.find_element(By.CSS_SELECTOR, "input#password")
    text_input.send_keys("secret_sauce")

    driver.find_element(By.CSS_SELECTOR, "input#login-button").click()

    driver.find_element(By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-onesie").click()
    driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()
    driver.find_element(By.CSS_SELECTOR, "button#checkout").click()

    text_input = driver.find_element(By.CSS_SELECTOR, "input#first-name")
    text_input.send_keys("Елена")

    text_input = driver.find_element(By.CSS_SELECTOR, "input#last-name")
    text_input.send_keys("Баглай")

    text_input = driver.find_element(By.CSS_SELECTOR, "input#postal-code")
    text_input.send_keys("602267")

    driver.find_element(By.CSS_SELECTOR, "#continue").click()

    total_cost = driver.find_element(By.CLASS_NAME, "summary_total_label").text
    total_cost_value = float(total_cost.split("$")[1])

    assert total_cost_value == 58.29, f"Итоговая сумма должна быть 58.29, но получена {total_cost_value}"

    driver.quit()