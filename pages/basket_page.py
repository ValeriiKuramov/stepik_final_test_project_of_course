from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_be_no_message_about_items_in_cart(self):
        # should be no message about the items in the cart
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), "Message about the items in the cart is displayed, but it should not be"

    def should_be_message_your_shopping_cart_is_empty(self):
        # check that there is a text stating that the basket is empty
        assert self.is_element_present(*BasketPageLocators.MESSAGE_YOUR_SHOPPING_CART_IS_EMPTY), "There is no text on the page stating that the shopping cart is empty"