from base.base_class import Base
from utilities.locators import CartPageLocators


class CartPage(Base):
    # Метод для проверки корректности страницы корзины
    def should_be_cart_page(self):
        assert self.browser.find_element(*CartPageLocators.CART_PAGE_NAME).text == 'YOUR CART', \
            'Wrong text!'
        assert self.browser.current_url() == 'https://www.saucedemo.com/cart.html',\
            'Wrong url address!'
