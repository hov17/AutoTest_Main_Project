from selenium.webdriver.common.by import By


class LoginPageLocators():
    USER_NAME_INPUT_FIELD = (By.XPATH, '//input[@id="user-name"]')
    PASSWORD_INPUT_FIELD = (By.XPATH, '//input[@id="password"]')
    LOGIN_BUTTON = (By.XPATH, '//input[@id="login-button"]')


class ProductPageLocators():
    MAIN_WORD = (By.XPATH, '//span[@class="title"]')
    GO_TO_CART_BUTTON = (By.XPATH, '//div[@id="shopping_cart_container"]')
    PRODUCT1_ADD_TO_CART_BUTTON = (By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')


class CartPageLocators():
    CART_PAGE_NAME = (By.XPATH, '//span[@class="title"]')
    CART_QUANTITY = (By.XPATH, '//div[@class="cart_quantity"]')
    CHECKOUT_BUTTON = (By.XPATH, '//button[@id="checkout"]')


class CheckoutInformationLocators():
    FIRST_NAME_INPUT_FIELD = (By.XPATH, '//input[@id="first-name"]')
    LAST_NAME_INPUT_FIELD = (By.XPATH, '//input[@id="last-name"]')
    POSTAL_CODE_INPUT_FIELD = (By.XPATH, '//input[@id="postal-code"]')
    CONTINUE_BUTTON = (By.XPATH, '//input[@id="continue"]')


class PaymentPageLocators():
    CART_QUANTITY = (By.XPATH, '//div[@class="cart_quantity"]')
    FINISH_BUTTON = (By.XPATH, '//button[@id="finish"]')


class FinishPageLocators():
    MAIN_LOGO = (By.XPATH, '//img[@class="pony_express"]')
