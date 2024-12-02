from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    LOGO_LOCATOR = (By.ID, "logo")
    MENU_ITEMS = (By.CLASS_NAME, "menu-item")
    WELCOME_MESSAGE = (By.CLASS_NAME, "welcome-text")

    def navi_to_homepage(self):
        """Navigate to home page"""
        self.driver.get("https://example.com")  # Replace with actual homepage URL

    def is_logo_displayed(self):
        """Check if logo is displayed"""
        logo = self.wait.until(EC.visibility_of_element_located(self.LOGO_LOCATOR))
        return logo.is_displayed()

    def get_welcome_message(self):
        """Get welcome message text"""
        welcome = self.wait.until(EC.presence_of_element_located(self.WELCOME_MESSAGE))
        return welcome.text