import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():

    # Initialize Firefox WebDriver
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.maximize_window()

    # Create wait object for convenience
    driver.wait = WebDriverWait(driver, 10)

    # Yield driver for test to use
    yield driver

    # Cleanup after test
    driver.close()
    driver.quit()


