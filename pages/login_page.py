from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message")

    def login_action(self, username, password):
        """Perform login action"""
        # Navigate to login page if needed
        self.driver.get("https://example.com/login")  # Replace with actual login URL

        username_field = self.wait.until(EC.element_to_be_clickable(self.USERNAME_INPUT))
        password_field = self.wait.until(EC.element_to_be_clickable(self.PASSWORD_INPUT))
        login_button = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))

        username_field.clear()
        username_field.send_keys(username)
        password_field.clear()
        password_field.send_keys(password)
        login_button.click()