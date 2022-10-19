from base.base_class import Base
from utilities.locators import CheckoutInformationLocators
from utilities.logger import Logger
import allure


class CheckoutInformationPage(Base):
    # Метод для заполнения информации о пользователе
    def filling_in_user_information(self, first_name, last_name, postal_code):
        with allure.step('Filling in information about user'):
            Logger.add_start_step(method='filling_in_user_information')
            self.browser.find_element(*CheckoutInformationLocators.FIRST_NAME_INPUT_FIELD).send_keys(first_name)
            print('Input firstname')
            self.browser.find_element(*CheckoutInformationLocators.LAST_NAME_INPUT_FIELD).send_keys(last_name)
            print('Input lastname')
            self.browser.find_element(*CheckoutInformationLocators.POSTAL_CODE_INPUT_FIELD).send_keys(postal_code)
            print('Input postal code')
            self.browser.find_element(*CheckoutInformationLocators.CONTINUE_BUTTON).click()
            print('Go to Payment page')
            Logger.add_end_step(self.browser.current_url, method='filling_in_user_information')
