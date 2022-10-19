from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_information import CheckoutInformationPage
from pages.payment_page import PaymentPage
from pages.finish_page import FinishPage
import allure


# Тест перехода в пустую Корзину со страницы Товаров
def test_should_be_successfully_go_to_empty_cart(browser):
    url = 'https://www.saucedemo.com/'
    page = LoginPage(browser, url, timeout=10)
    page.open()
    page.authorization('standard_user', 'secret_sauce')
    page = ProductPage(browser, browser.current_url, timeout=10)
    page.go_to_cart()
    page = CartPage(browser, browser.current_url, timeout=10)
    page.should_be_cart_page()


# Тест покупки товара
@allure.description('Test of buying one product')
def test_should_be_successfully_buy_of_product1(browser):
    url = 'https://www.saucedemo.com/'
    page = LoginPage(browser, url, timeout=10)
    page.open()
    page.authorization('standard_user', 'secret_sauce')
    page = ProductPage(browser, browser.current_url, timeout=10)
    page.add_product1_to_cart()
    page.go_to_cart()
    page = CartPage(browser, browser.current_url, timeout=10)
    page.should_be_cart_page_with_one_added_product()
    page.go_to_checkout_information_page()
    page = CheckoutInformationPage(browser, browser.current_url, timeout=10)
    page.filling_in_user_information('Ivan', 'Ivanov', '123456')
    page = PaymentPage(browser, browser.current_url, timeout=10)
    page.confirmation_of_payment_for_the_order_with_1_product()
    page = FinishPage(browser, browser.current_url, timeout=10)
    page.should_be_correct_finish_page()
    page.get_screenshot()


# Тест перехода на страницу About
def test_open_about_link(browser):
    url = 'https://www.saucedemo.com/'
    page = LoginPage(browser, url, timeout=10)
    page.open()
    page.authorization('standard_user', 'secret_sauce')
    page = ProductPage(browser, browser.current_url, timeout=10)
    page.go_to_about_page()
    page.should_correct_url('https://saucelabs.com/')
    page.get_screenshot()
