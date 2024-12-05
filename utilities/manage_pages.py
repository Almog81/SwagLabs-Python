import pytest

from pages.create_user_page import CreateUserPage
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
            self.create_user_page = CreateUserPage(driver)

    return Pages(driver)
