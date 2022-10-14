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
