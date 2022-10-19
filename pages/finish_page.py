from base.base_class import Base
from utilities.locators import FinishPageLocators
from utilities.logger import Logger
import allure


class FinishPage(Base):
    # Метод для проверки корректности страницы
    def should_be_correct_finish_page(self):
        with allure.step('Should be correct finish page'):
            Logger.add_start_step(method='should_be_correct_finish_page')
            assert self.is_element_present(*FinishPageLocators.MAIN_LOGO), 'Main Logo is missing!'
            assert self.browser.current_url == 'https://www.saucedemo.com/checkout-complete.html', 'Wrong URL!'
            Logger.add_end_step(self.browser.current_url, method='should_be_correct_finish_page')
