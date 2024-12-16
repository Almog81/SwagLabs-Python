import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from utilities.ui_actions import UiActions


class CreateUserPage(UiActions):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    txt_firstName = (By.ID, "firstname")
    txt_lastName = (By.ID, "lastname")
    txt_email = (By.ID, "email_address")
    txt_password = (By.ID, "password")
    txt_passwordConfirmation = (By.ID, "password-confirmation")
    btn_submit = (By.CSS_SELECTOR, ".action.submit.primary")
    elm_messageSuccess = (By.CLASS_NAME, "message-success")
    elm_messageError = (By.CLASS_NAME, "message-error")

    def create_user_action(self, user_data):
        self.fill_action(self.txt_firstName,user_data["firstName"])
        self.fill_action(self.txt_lastName, user_data["lastName"])
        self.fill_action(self.txt_email, user_data["email"])
        self.fill_action(self.txt_password, user_data["Password"])
        self.fill_action(self.txt_passwordConfirmation, user_data["Password"])
        self.click_action(self.btn_submit)

    def get_message(self):
        try:
            self.is_element_visible(self.elm_messageSuccess)
            return self.get_text(self.elm_messageSuccess)
        except TimeoutException:
            return self.get_text(self.elm_messageError)

    def verify_user_created(self):
        self.wait_for_page_load()
        assert self.get_message() == "Thank you for registering with Main Website Store.", f"Failed TO Crate new user: {self.get_text(self.elm_messageError)}"
