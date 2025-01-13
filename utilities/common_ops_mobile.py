import time

import pytest
from appium import webdriver
import json

@pytest.fixture
def mobile_driver():
    devices = read_from_json("MobileDevices.json")["devices"]
    desired_caps = devices["OnePlus3"]
    driver = webdriver.Remote("http://127.0.0.1:4723", desired_caps)

    # Yield driver for the test to use
    yield driver

    # Cleanup after test
    driver.quit()

def read_from_json(file_path):
    with open("../DDTFiles/" + file_path, "r") as file:
        return json.load(file)
