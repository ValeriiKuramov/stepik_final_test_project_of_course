from .pages.main_page import MainPage
from .pages.login_page import LoginPage

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