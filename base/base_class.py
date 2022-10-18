import datetime
from selenium.common.exceptions import NoSuchElementException
from utilities.logger import Logger


class Base():
    def __init__(self, browser, url, timeout):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # Метод открывающий браузер в полном окне
    def open(self):
        Logger.add_start_step(method='open')
        self.browser.get(self.url)
        self.browser.maximize_window()
        print('Open browser')
        Logger.add_end_step(self.browser.current_url, method='open')

    # Метод получения текущего адреса URL
    def get_current_url(self):
        get_url = self.browser.current_url
        print(f'Current URL: {get_url}')

    # Метод для проверки корректность URL
    def should_correct_url(self, correct_url):
        assert self.browser.current_url == correct_url, 'Wrong url!'

    # Метод для получения скриншота страницы
    def get_screenshot(self):
        Logger.add_start_step(method='get_screenshot')
        name_screenshot = 'screenshot-' + str(datetime.datetime.utcnow().strftime("%d.%m.%Y.%H.%M.%S")) + '.png'
        self.browser.save_screenshot('C:\\Users\\Эмиль\\pythonProject\\AutoTest_Main_Project\\screen\\'
                                     + name_screenshot)
        print('Get screenshot')
        Logger.add_end_step(self.browser.current_url, method='get_screenshot')

    # Метод для проверки элемента на странице
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
