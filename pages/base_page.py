class BasePage():

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        # open the desired page in the browser
        self.browser.get(self.url)
    