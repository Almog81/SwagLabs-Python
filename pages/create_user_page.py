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
    txt_firstName = (By.ID, "customer.firstName")
    txt_lastName = (By.ID, "customer.lastName")
    txt_address = (By.ID, "customer.address.street")
    txt_city = (By.ID, "customer.address.city")
    txt_state = (By.ID, "customer.address.state")
    txt_zipCode = (By.ID, "customer.address.zipCode")
    txt_phoneNumber = (By.ID, "customer.phoneNumber")
    txt_ssn = (By.ID, "customer.ssn")

    txt_username = (By.ID, "customer.username")
    txt_password = (By.ID, "customer.password")
    txt_passwordConfirmation = (By.ID, "repeatedPassword")
    btn_submit = (By.XPATH, "//*[@value=\"Register\"]")

    elm_messageSuccess = (By.CLASS_NAME, "message-success")
    elm_messageError = (By.CLASS_NAME, "message-error")

    def create_user_action(self, user_data):
        self.fill_action(self.txt_firstName,user_data["firstName"])
        self.fill_action(self.txt_lastName, user_data["lastName"])
        self.fill_action(self.txt_address, user_data["address"])
        self.fill_action(self.txt_city, user_data["city"])
        self.fill_action(self.txt_state, user_data["state"])
        self.fill_action(self.txt_zipCode, user_data["zipCode"])
        self.fill_action(self.txt_phoneNumber, user_data["phone"])
        self.fill_action(self.txt_ssn, user_data["ssn"])
        self.fill_action(self.txt_username, user_data["username"])
        self.fill_action(self.txt_password, user_data["password"])
        self.fill_action(self.txt_passwordConfirmation, user_data["password"])
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
