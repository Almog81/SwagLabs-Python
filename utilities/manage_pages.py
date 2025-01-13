from pages.cart_page import CartPage
from utilities.common_ops import *
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.fixture
def pages(driver):
    """Initialize all page objects"""
    class Pages:
        def __init__(self, driver):
            self.home_page = HomePage(driver)
            self.login_page = LoginPage(driver)
            self.cart_page = CartPage(driver)
            self.login_page.home_page = self.home_page
            self.home_page.login_page = self.login_page
            self.cart_page.home_page = self.home_page
            self.home_page.cart_page = self.cart_page

    return Pages(driver)
