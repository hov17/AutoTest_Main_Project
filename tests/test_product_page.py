# Тест на успешный переход в корзину
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage


def test_should_be_successfully_go_to_cart(browser):
    url = 'https://www.saucedemo.com/'
    page = LoginPage(browser, url, timeout=10)
    page.open()
    page.authorization('standard_user', 'secret_sauce')
    page = ProductPage(browser, browser.current_url, timeout=10)
    page.go_to_cart()
    page = CartPage(browser, browser.current_url, timeout=10)
    page.should_be_cart_page()
