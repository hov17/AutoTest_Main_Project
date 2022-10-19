from base.base_class import Base
from utilities.locators import CartPageLocators
from utilities.logger import Logger
import allure


class CartPage(Base):
    # Метод для перехода на страницу Checkout
    def go_to_checkout_information_page(self):
        with allure.step('Go to Checkout Information page'):
            Logger.add_start_step(method='go_to_checkout_information_page')
            self.browser.find_element(*CartPageLocators.CHECKOUT_BUTTON).click()
            print('Go to Checkout Information page')
            Logger.add_end_step(self.browser.current_url, method='go_to_checkout_information_page')

    # Метод для проверки корректности страницы Корзины
    def should_be_cart_page(self):
        Logger.add_start_step(method='should_be_cart_page')
        assert self.browser.current_url == 'https://www.saucedemo.com/cart.html', 'Wrong URL address!'
        assert self.browser.find_element(*CartPageLocators.CART_PAGE_NAME).text == 'YOUR CART', 'Wrong text!'
        Logger.add_end_step(self.browser.current_url, method='should_be_cart_page')

    # Метод для проверки корректности страницы Корзины с 1-м товаром
    def should_be_cart_page_with_one_added_product(self):
        with allure.step('Should be cart page with one added product'):
            Logger.add_start_step(method='should_be_cart_page_with_one_added_product')
            assert self.browser.current_url == 'https://www.saucedemo.com/cart.html', 'Wrong URL address!'
            assert self.browser.find_element(*CartPageLocators.CART_PAGE_NAME).text == 'YOUR CART', 'Wrong text!'
            assert self.browser.find_element(*CartPageLocators.CART_QUANTITY).text == '1',\
                'Wrong quantity of products in Cart!'
            print('Cart page is correct')
            Logger.add_end_step(url=self.browser.current_url, method='should_be_cart_page_with_one_added_product')
