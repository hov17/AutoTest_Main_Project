class Base():
    def __init__(self, browser, url, timeout):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # Метод открывающий браузер в полном окне
    def open(self):
        self.browser.get(self.url)
        self.browser.maximize_window()

