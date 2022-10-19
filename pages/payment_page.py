from base.base_class import Base
from utilities.locators import PaymentPageLocators
from utilities.logger import Logger
import allure


class PaymentPage(Base):
    # Метод подтверждения оплаты заказа на 1 товар
    def confirmation_of_payment_for_the_order_with_1_product(self):
        with allure.step('Confirmation of payment for the order with 1 product'):
            Logger.add_start_step(method='confirmation_of_payment_for_the_order_with_1_item')
            assert self.browser.find_element(*PaymentPageLocators.CART_QUANTITY).text == '1', \
                'Wrong number of items in cart!'
            self.browser.find_element(*PaymentPageLocators.FINISH_BUTTON).click()
            print('Order purchase completed')
            Logger.add_end_step(self.browser.current_url, method='confirmation_of_payment_for_the_order_with_1_item')
