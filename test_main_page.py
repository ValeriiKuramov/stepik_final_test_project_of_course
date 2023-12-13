from .pages.main_page import MainPage
from selenium.webdriver.common.by import By

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"

    page = MainPage(browser, link) # initialize the Page Object, pass the driver instance and the url to the constructor
    page.open()  # opening the page
    page.go_to_login_page() # executing the page method — go to the login page

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()