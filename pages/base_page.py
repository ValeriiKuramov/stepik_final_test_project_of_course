import math
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

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

    def get_element_text(self, how, what):
        # return the text of the element
        text_of_element = ""
        try:
            element = self.browser.find_element(how, what)
            text_of_element = element.text
        except Exception:
            pass
        return text_of_element.strip()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")