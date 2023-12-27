import math
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
from .locators import BasketPageLocators


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

    def is_not_element_present(self, how, what, timeout=4):
        # checking that the element does not appear on the page for a specified time
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        # checking that the element disappears
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def go_to_login_page(self):
        # looking for a link to the login page and click
        #link = self.browser.find_element(*BasePageLocators.LOGIN_LINK_INVALID)
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        # check the presence of the element specified in the parameters
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_basket_page(self):
        # looking for a link to the  basket page and click
        basket_link = self.browser.find_element(*BasketPageLocators.BASKET_LINK)
        basket_link.click()