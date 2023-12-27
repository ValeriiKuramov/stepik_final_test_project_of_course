from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_product_to_cart(self):
        # adding a product to the cart
        button_add_to_cart = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_CART)
        button_add_to_cart.click()

    def should_be_product_name_in_page(self):
        # check if the product name is on the page
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_IN_PAGE), "Product neme in page is not presented"

    def should_be_product_price_in_page(self):
        # check if the product name is on the page
        assert self.is_element_present(*ProductPageLocators.PRICE_IN_PAGE), "Product price in page is not presented"

    def should_be_product_name_in_message(self):
        # check if the product name is on the page
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE), "Product name in message is not presented"

    def should_be_product_price_in_message(self):
        # check if the product name is on the page
        assert self.is_element_present(*ProductPageLocators.PRICE_IN_MESSAGE), "Product price in message is not presented"

    def should_be_product_names_must_match(self):
        # product name in the message must match the product that you actually added
        product_name_in_page = self.get_element_text(*ProductPageLocators.PRODUCT_NAME_IN_PAGE)
        product_name_in_message = self.get_element_text(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE)
        assert product_name_in_page == product_name_in_message, "The product name in the message must match the product that you actually added"

    def should_be_product_price_must_match(self):
        # cost of the basket must match the price of the product
        product_price_in_page = self.get_element_text(*ProductPageLocators.PRICE_IN_PAGE)
        product_price_in_message = self.get_element_text(*ProductPageLocators.PRICE_IN_MESSAGE)
        assert product_price_in_page == product_price_in_message, "The cost of the basket must match the price of the product"

    def should_not_be_success_message(self):
        # success message should not be displayed
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_be_disappearing_element(self):
        # check that the element disappears
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "The message about adding the product to the cart has not disappeared"
