from selenium.common.exceptions import NoSuchElementException


class BasePage():
    def __init__(self, browser, url, timeout=10):  #Конструктор — метод, который вызывается, когда мы создаем объект. Конструктор объявляется ключевым словом __init__
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)


    def open(self):
        self.browser.get(self.url)


    def is_element_present(self, CSS_SELECTOR, login_link):
        try:
            self.browser.find_element(CSS_SELECTOR, login_link)
        except (NoSuchElementException):
            return False
        return True
