from base.base_class import Base
from utilities.locators import LoginPageLocators


class LoginPage(Base):

    # Метод для авторизации пользователя
    def authorization(self, username, password):
        self.browser.find_element(*LoginPageLocators.USER_NAME_INPUT_FIELD).send_keys(username)
        print('Input username')
        self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT_FIELD).send_keys(password)
        print('Input password')
        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        print('Click login button')
