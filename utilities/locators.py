from selenium.webdriver.common.by import By


class LoginPageLocators():
    USER_NAME_INPUT_FIELD = (By.XPATH, '//input[@id="user-name"]')
    PASSWORD_INPUT_FIELD = (By.XPATH, '//input[@id="password"]')
    LOGIN_BUTTON = (By.XPATH, '//input[@id="login-button"]')


class ProductPageLocators():
    GO_TO_CART_BUTTON = (By.XPATH, '//div[@id="shopping_cart_container"]')
    MAIN_WORD = (By.XPATH, '//span[@class="title"]')


class CartPageLocators():
    CART_PAGE_NAME = (By.XPATH, '//span[@class="title"]')
