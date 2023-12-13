from selenium.common.exceptions import NoSuchElementException
class BasePage():

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        # open the desired page in the browser
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        # checking the presence of the element
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
