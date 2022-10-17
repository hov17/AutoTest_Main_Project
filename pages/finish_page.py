from base.base_class import Base
from utilities.locators import FinishPageLocators


class FinishPage(Base):
    # Метод для проверки корректности страницы
    def should_be_correct_finish_page(self):
        self.is_element_present(*FinishPageLocators.MAIN_LOGO), 'Main Logo is missing!'
        assert self.browser.current_url == 'https://www.saucedemo.com/checkout-complete.html', 'Wrong URL!'
