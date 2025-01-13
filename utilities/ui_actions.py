from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.common_ops import driver
from appium.webdriver.webdriver import WebDriver as AppiumWebDriver
from selenium.webdriver.support.select import Select

class UiActions:
    def __init__(self, driver, wait_time=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_time)

    def wait_for_page_load(self, timeout=30):
        try:
            if isinstance(self.driver, AppiumWebDriver):  # For mobile tests
                WebDriverWait(self.driver, timeout).until(
                    lambda driver: driver.current_activity is not None and driver.current_activity != ''
                )
            else:  # For web tests
                WebDriverWait(self.driver, timeout).until(
                    lambda driver: driver.execute_script("return document.readyState") == "complete"
                )
        except TimeoutException:
            raise TimeoutException("The page did not load completely within the timeout period.")

    def fill_action(self, locator, text):
        field = self.wait.until(EC.visibility_of_element_located(locator))
        field.clear()
        field.send_keys(text)

    def click_action(self, locator):
        button = self.wait.until(EC.element_to_be_clickable(locator))
        button.click()
        self.wait_for_page_load()

    def drop_down_select(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))

        if isinstance(self.driver, AppiumWebDriver):
            element.click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//*[@text='{text}']"))).click()
            return

        try:
            Select(element).select_by_visible_text(text)
        except:
            element.send_keys(text)

    def is_element_visible(self, locator):
        self.wait_for_page_load()
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def get_text(self, locator):
        self.wait_for_page_load()
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def check_broken_images(self, locator):
        broken_images = []
        images = self.driver.find_elements(*locator)
        for img in images:
            src = img.get_attribute("src")
            if not src or "invalid" in src:
                broken_images.append(img)
        return broken_images

    def get_page_load_time(self):
        navigation_start = self.driver.execute_script("return window.performance.timing.navigationStart")
        load_event_end = self.driver.execute_script("return window.performance.timing.loadEventEnd")
        load_time = (load_event_end - navigation_start) / 1000  # Convert to seconds
        return load_time

    def get_elements_by_locator(self, locator):
        self.is_element_visible(locator)
        return self.driver.find_elements(*locator)