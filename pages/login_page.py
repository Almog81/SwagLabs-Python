from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from utilities.ui_actions import UiActions


class LoginPage(UiActions):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    txt_loginUsername = (By.NAME, "username")
    txt_password = (By.NAME, "password")
    btn_login = (By.XPATH, "//*[@value=\"Log In\"]")

    def login_action(self,  login_data):
        self.fill_action(self.txt_loginUsername, login_data["username"])
        self.fill_action(self.txt_password,  login_data["password"])
        self.click_action(self.btn_login)
