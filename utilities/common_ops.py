import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
import json


@pytest.fixture
def driver():

    # Initialize Firefox WebDriver
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.maximize_window()

    # Create wait object for convenience
    driver.wait = WebDriverWait(driver, 20)

    # Yield driver for test to use
    yield driver

    # Cleanup after test
    driver.close()
    driver.quit()



def read_from_json(file_path):
    with open("../DDTFiles/" + file_path, "r") as file:
        return json.load(file)