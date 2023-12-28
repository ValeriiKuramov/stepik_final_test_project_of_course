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

    def register_new_user(self, email, password):
        # performing user registration
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_ADDRESS_REGISTRATION)
        email_input.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTRATION)
        password_input.send_keys(password)
        password_input_cofirm = self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTRATION_CONFIRMATION)
        password_input_cofirm.send_keys(password)
        button_registration = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        button_registration.click()


