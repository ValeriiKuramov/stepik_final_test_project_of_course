from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):
    def go_to_login_page(self):
        #  looking for a link to the login page and click
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        # check the presence of the element specified in the parameters
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
