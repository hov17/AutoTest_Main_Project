from base.base_class import Base
from utilities.locators import LoginPageLocators


class LoginPage(Base):

    # Метод для авторизации пользователя
    def authorization(self, username, password):
        self.browser.find_element(*LoginPageLocators.USER_NAME_INPUT_FIELD).send_keys(username)
        self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
