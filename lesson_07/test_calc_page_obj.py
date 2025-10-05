import pytest
from selenium import webdriver
from CalcPage import CalcPage
from time import sleep

@pytest.fixture
def driver():
     driver = webdriver.Chrome()
     driver.implicitly_wait(5)
     driver.maximize_window()
     yield driver
     driver.quit()

def test_calc(driver):
    calc_page = CalcPage(driver)
    calc_page.open()
    calc_page.do_calc()
    sleep(5)
    calc_page.scroll_down()
    calc_page.perform_element()
    sleep(5)
    calc_page.wait_for_result()
    result = calc_page.get_result()
    print(result)