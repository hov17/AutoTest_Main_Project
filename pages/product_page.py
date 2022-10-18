from base.base_class import Base
from utilities.locators import ProductPageLocators
from utilities.logger import Logger


class ProductPage(Base):
    # Метод для перехода на страницу корзины
    def go_to_cart(self):
        Logger.add_start_step(method='go_to_cart')
        self.browser.find_element(*ProductPageLocators.GO_TO_CART_BUTTON).click()
        print('Go to Cart page')
        Logger.add_end_step(self.browser.current_url, method='go_to_cart')

    # Метод проверяющий переход на страницу с товарами
    def should_be_product_page(self):
        assert self.browser.find_element(*ProductPageLocators.MAIN_WORD).text == 'PRODUCTS', 'Wrong text!'
        assert self.browser.current_url == 'https://www.saucedemo.com/inventory.html', 'Wrong URL!'

    # Метод на добавление товара и перехода в корзину
    def add_product1_to_cart(self):
        Logger.add_start_step(method='add_product1_to_cart')
        self.browser.find_element(*ProductPageLocators.PRODUCT1_ADD_TO_CART_BUTTON).click()
        assert self.browser.find_element(*ProductPageLocators.GO_TO_CART_BUTTON).text == '1', \
            'Add product to Cart!'
        print('Product added to Cart')
        Logger.add_end_step(self.browser.current_url, method='add_product1_to_cart')

    # Метод перехода на страницу About
    def go_to_about_page(self):
        self.browser.find_element(*ProductPageLocators.BURGER_MENU).click()
        self.browser.find_element(*ProductPageLocators.ABOUT_LINK).click()
        print('Click About link')
