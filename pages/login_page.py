from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from utilities.ui_actions import UiActions


class LoginPage(UiActions):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    txt_loginEmail = (By.ID, "email")
    txt_password = (By.ID, "pass")
    btn_login = (By.CSS_SELECTOR, ".action.login.primary")

    def login_action(self, email, password):
        self.fill_action(self.txt_loginEmail, email)
        self.fill_action(self.txt_password, password)
        self.click_action(self.btn_login)
