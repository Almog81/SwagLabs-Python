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
    txt_password = (By.ID, "passwd")
    btn_login = (By.ID, "SubmitLogin")
    elm_user_info = (By.CLASS_NAME, "header_user_info")

    txt_emailCreate = (By.ID, "email_create")
    btn_submitCrate = (By.ID, "SubmitCreate")
    elm_crateAccountError = (By.CLASS_NAME, "create_account_error")

    def login_action(self, email, password):
        self.fill_action(self.txt_loginEmail, email)
        self.fill_action(self.txt_password, password)
        self.click_action(self.btn_login)

    def get_user_name(self):
        self.is_element_visible(self.elm_user_info)
        return self.get_text(self.elm_user_info)

