from pages.login_page import LoginPage
from pages.product_page import ProductPage


# Тест авторизации за стандартного пользователя
def test_should_be_successfully_authorization(browser):
    url = 'https://www.saucedemo.com/'
    page = LoginPage(browser, url, timeout=10)
    page.open()
    page.get_current_url()
    page.authorization('standard_user', 'secret_sauce')
    page = ProductPage(browser, browser.current_url, timeout=10)
    page.should_be_product_page()
