from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_guest_can_add_product_to_basket(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
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

