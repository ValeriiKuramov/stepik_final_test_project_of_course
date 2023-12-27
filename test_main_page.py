from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link) # initialize the Page Object, pass the driver instance and the url to the constructor
    page.open()  # opening the page
    page.go_to_login_page() # executing the page method — go to the login page
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    main_page = MainPage(browser, link) # initialize the Page Object, pass the driver instance and the url to the constructor
    main_page.open()  # opening the page
    main_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_no_message_about_items_in_cart()
    basket_page.should_be_message_your_shopping_cart_is_empty()
