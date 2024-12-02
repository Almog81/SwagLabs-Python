import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait

# Global page objects to be initialized once
home_page = None
login_page = None


class PageObjectManager:
    """
    Manages page objects and provides centralized initialization
    """

    @classmethod
    def init_pages(cls, driver):
        """
        Initialize global page objects
        """
        global home_page, login_page

        from pages.home_page import HomePage
        from pages.login_page import LoginPage

        home_page = HomePage(driver)
        login_page = LoginPage(driver)


@pytest.fixture(scope="function")
def driver():
    """
    Fixture to initialize and manage WebDriver
    """
    # Initialize Firefox WebDriver
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.maximize_window()

    # Create wait object for convenience
    driver.wait = WebDriverWait(driver, 10)

    # Initialize global page objects
    PageObjectManager.init_pages(driver)

    # Navigate to base URL (replace with your actual base URL)
    driver.get("https://example.com")

    # Yield driver for test to use
    yield driver

    # Cleanup after test
    driver.close()
    driver.quit()