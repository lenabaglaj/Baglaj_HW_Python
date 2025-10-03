import pytest
from selenium import webdriver
from IntPage import IntPage
from MainPage import MainPage
from CartPage import CartPage
from CheckoutPage import CheckoutPage
from time import sleep

@pytest.fixture
def driver():
     driver = webdriver.Firefox()
     driver.maximize_window()
     driver.implicitly_wait(5)
     driver.get("https://www.saucedemo.com/")
     yield driver
     driver.quit()

def test_page(driver):
    int_page = IntPage(driver)
    int_page.do_int()
    sleep(5)

    main_page = MainPage(driver)
    main_page.get_shop()
    sleep(5)

    cart_page = CartPage(driver)
    cart_page.shop_cart()
    sleep(5)

    checkout_page = CheckoutPage(driver)
    checkout_page.made_cart()

    assert checkout_page.get_total_amount() == 58.29