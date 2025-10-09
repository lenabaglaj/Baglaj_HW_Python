from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_auth_2():
    # Переход на сайт
    driver = webdriver.Chrome()
    driver.get("https://fstravel.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)

    # Ожидание и клик по первой кнопке
    #first_button = WebDriverWait(driver, 30).until(
    #   EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "popmechanic-close")]'))
    #)
    #first_button.click()

    # Ожидание и клик по второй кнопке
    second_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//*[contains(@class, "v-icon-user-14")]'))
    )
    second_button.click()

    # Ввод имени пользователя
    username_input = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#email')))

    username_input.clear()  # Очистка поля перед вводом
    username_input.send_keys("dan4@yandex.ru")


  # Ввод пароля
    password_input = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#password'))
    )
    password_input.clear()  # Очистка поля перед вводом
    password_input.send_keys("Alina2011")

    # Ожидание и клик по кнопке входа
    login_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//input[contains(@class, "new-button")]'))
    )
    assert login_button.is_enabled()


    # Закрытие браузера
    driver.quit()