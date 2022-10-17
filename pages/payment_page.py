from base.base_class import Base
from utilities.locators import PaymentPageLocators


class PaymentPage(Base):
    # Метод подтверждения оплаты заказа на 1 товар
    def confirmation_of_payment_for_the_order_with_1_item(self):
        assert self.browser.find_element(*PaymentPageLocators.CART_QUANTITY).text == '1', \
            'Wrong number of items in cart!'
        self.browser.find_element(*PaymentPageLocators.FINISH_BUTTON).click()
        print('Order purchase completed')
