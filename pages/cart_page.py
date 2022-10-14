from base.base_class import Base
from utilities.locators import CartPageLocators


class CartPage(Base):
    # Метод для перехода на страницу Checkout
    def go_to_checkout_page(self):
        self.browser.find_element(*CartPageLocators.CHECKOUT_BUTTON).click()
        print('Go to Checkout page')

    # Метод для проверки корректности страницы Корзины
    def should_be_cart_page(self):
        assert self.browser.current_url == 'https://www.saucedemo.com/cart.html', 'Wrong URL address!'
        assert self.browser.find_element(*CartPageLocators.CART_PAGE_NAME).text == 'YOUR CART', 'Wrong text!'

    # Метод для проверки корректности страницы Корзины с 1-м товаром
    def should_be_cart_page_with_one_added_product(self):
        assert self.browser.current_url == 'https://www.saucedemo.com/cart.html', 'Wrong URL address!'
        assert self.browser.find_element(*CartPageLocators.CART_PAGE_NAME).text == 'YOUR CART', 'Wrong text!'
        assert self.browser.find_element(*CartPageLocators.CART_QUANTITY).text == '1',\
            'Wrong quantity of products in Cart!'
        print('Cart page is correct')
