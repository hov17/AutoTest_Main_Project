from base.base_class import Base
from utilities.locators import ProductPageLocators


class ProductPage(Base):
    # Переход в корзину
    def go_to_cart(self):
        self.browser.find_element(*ProductPageLocators.GO_TO_CART_BUTTON).click()
