from base.base_class import Base
from utilities.locators import ProductPageLocators


class ProductPage(Base):
    # Переход в корзину
    def go_to_cart(self):
        self.browser.find_element(*ProductPageLocators.GO_TO_CART_BUTTON).click()
        print('Go to Cart page')

    # Метод проверяющий переход на страницу с товарами
    def should_be_product_page(self):
        assert self.browser.find_element(*ProductPageLocators.MAIN_WORD).text == 'PRODUCTS', 'Wrong text!'
        assert self.browser.current_url == 'https://www.saucedemo.com/inventory.html', 'Wrong URL!'

