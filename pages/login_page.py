from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # checking for the correct url
        assert "/login" in self.browser.current_url, "Invalid url for the login form"

    def should_be_login_form(self):
        # checking the availability of the login form
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # checking the availability of the registration form on the page
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login register form is not presented"
