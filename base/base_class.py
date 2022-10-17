import datetime
from selenium.common.exceptions import NoSuchElementException


class Base():
    def __init__(self, browser, url, timeout):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # Метод открывающий браузер в полном окне
    def open(self):
        self.browser.get(self.url)
        self.browser.maximize_window()
        print('Open browser')

    # Метод получения текущего адреса URL
    def get_current_url(self):
        get_url = self.browser.current_url
        print(f'Current URL: {get_url}')

    # Метод для получения скриншота страницы
    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%d.%m.%Y.%H.%M.%S")
        screenshot_name = 'screenshot' + now_date + '.png'
        self.browser.save_screenshot('.\\screen\\' + screenshot_name)
        print('Get screenshot')

    # Метод для проверки элемента на странице
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
