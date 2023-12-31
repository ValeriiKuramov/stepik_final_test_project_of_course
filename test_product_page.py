import time
import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

link_promo = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
link_not_promo = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"

@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  #pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    # check that after opening the page there is no message about the successful addition to the cart
    product_page.should_not_be_success_message()
    # adding a product to the cart
    product_page.add_product_to_cart()
    product_page.solve_quiz_and_get_code()
    # check the availability of the product name on the page
    product_page.should_be_product_name_in_page()
    # check the availability of the product price on the page
    product_page.should_be_product_price_in_page()
    # check the presence of the product name in the message block
    product_page.should_be_product_name_in_message()
    # check the presence of the product price in the message block
    product_page.should_be_product_price_in_message()
    # product name in the message must match the product that you actually added
    product_page.should_be_product_names_must_match()
    # cost of the basket must match the price of the product
    product_page.should_be_product_price_must_match()

@pytest.mark.skip(reason="currently skipping this test")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, link_not_promo)
    product_page.open()
    # adding a product to the cart
    product_page.add_product_to_cart()
    # check that after opening the page there is no message about the successful addition to the cart
    product_page.should_not_be_success_message()

@pytest.mark.skip(reason="currently skipping this test")
def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser, link_not_promo)
    product_page.open()
    # check that after opening the page there is no message about the successful addition to the cart
    product_page.should_not_be_success_message()

@pytest.mark.skip(reason="currently skipping this test")
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, link_not_promo)
    product_page.open()
    # adding a product to the cart
    product_page.add_product_to_cart()
    # checking the disappearance of messages
    product_page.should_be_disappearing_element()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_login_page()
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_no_message_about_items_in_cart()
    basket_page.should_be_message_your_shopping_cart_is_empty()

@pytest.mark.user_registration
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # opening the registration page
        link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        login_page = LoginPage(browser, link)
        login_page.open()
        # creating fake values email and password
        email = str(time.time()) + "@fakemail.org"
        password = "7mNx5dRLz".join(str(time.time()))
        # registering a new user
        login_page.register_new_user(email, password)
        # check that the user is registered
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, link_promo)
        product_page.open()
        # check that after opening the page there is no message about the successful addition to the cart
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, link_promo)
        product_page.open()
        # check that after opening the page there is no message about the successful addition to the cart
        product_page.should_not_be_success_message()
        # adding a product to the cart
        product_page.add_product_to_cart()
        product_page.solve_quiz_and_get_code()
        # check the availability of the product name on the page
        product_page.should_be_product_name_in_page()
        # check the availability of the product price on the page
        product_page.should_be_product_price_in_page()
        # check the presence of the product name in the message block
        product_page.should_be_product_name_in_message()
        # check the presence of the product price in the message block
        product_page.should_be_product_price_in_message()
        # product name in the message must match the product that you actually added
        product_page.should_be_product_names_must_match()
        # cost of the basket must match the price of the product
        product_page.should_be_product_price_must_match()