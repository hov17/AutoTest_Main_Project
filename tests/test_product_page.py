from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage


# Тест перехода в пустую Корзины со страницы Товаров
def test_should_be_successfully_go_to_empty_cart(browser):
    url = 'https://www.saucedemo.com/'
    page = LoginPage(browser, url, timeout=10)
    page.open()
    page.get_current_url()
    page.authorization('standard_user', 'secret_sauce')
    page = ProductPage(browser, browser.current_url, timeout=10)
    page.go_to_cart()
    page = CartPage(browser, browser.current_url, timeout=10)
    page.should_be_cart_page()


# Тест на добавления товара в корзину
def test_should_be_successfully_add_to_cart(browser):
    url = 'https://www.saucedemo.com/'
    page = LoginPage(browser, url, timeout=10)
    page.open()
    page.get_current_url()
    page.authorization('standard_user', 'secret_sauce')
    page = ProductPage(browser, browser.current_url, timeout=10)
    page.add_product1_to_cart()
    page.go_to_cart()
    page = CartPage(browser, browser.current_url, timeout=10)
    page.should_be_cart_page_with_one_added_product()
