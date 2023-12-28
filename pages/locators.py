from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_ADDRESS_REGISTRATION = (By.CSS_SELECTOR, "#register_form [name='registration-email']")
    PASSWORD_REGISTRATION = (By.CSS_SELECTOR, '#register_form [name="registration-password1"]')
    PASSWORD_REGISTRATION_CONFIRMATION = (By.CSS_SELECTOR, '#register_form [name="registration-password2"]')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, '#register_form [name="registration_submit"]')


class ProductPageLocators():
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME_IN_PAGE = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_IN_PAGE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, "#messages strong")
    PRICE_IN_MESSAGE = (By.CSS_SELECTOR, ".alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) > .alertinner")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class  BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, ".page_inner .btn.btn-default:nth-child(1)")
    PRODUCT_IN_BASKET_INVALID = (By.CSS_SELECTOR, ".page-header.action > h1")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#content_inner .row:nth-child(1) h2")
    MESSAGE_YOUR_SHOPPING_CART_IS_EMPTY = (By.CSS_SELECTOR, ".content > #content_inner > p")
