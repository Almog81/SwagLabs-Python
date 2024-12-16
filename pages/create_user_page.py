import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from utilities.ui_actions import UiActions


class CreateUserPage(UiActions):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    txt_emailCreate = (By.ID, "email_create")
    btn_submitCrate = (By.ID, "SubmitCreate")
    elm_crateAccountError = (By.ID, "create_account_error")

    male = (By.ID, "id_gender1")
    female = (By.ID, "id_gender2")
    txt_customerFirstname = (By.ID, "customer_firstname")
    txt_customerLastname = (By.ID, "customer_lastname")
    txt_userPassword = (By.ID, "passwd")
    drop_days = (By.ID , "days")
    drop_months = (By.ID, "months")
    drop_years = (By.ID, "years")
    box_newsletter = (By.ID , "newsletter")
    btn_submit_account = (By.ID, "submitAccount")

    def create_user_action(self, user_data):
        self.fill_action(self.txt_emailCreate,user_data["email"] )
        self.click_action(self.btn_submitCrate)
        #TODO gender function
        self.click_action(self.male)
        self.fill_action(self.txt_customerFirstname,user_data["firstName"])
        self.fill_action(self.txt_customerLastname, user_data["lastName"])
        self.fill_action(self.txt_userPassword, user_data["userPassword"])
        self.drop_down_select(self.drop_days, user_data["day"])
        self.drop_down_select(self.drop_months, user_data["month"])
        self.drop_down_select(self.drop_years, user_data["year"])
        self.click_action(self.box_newsletter)
        # self.click_action(self.btn_submit_account)

    def get_error(self):
        self.is_element_visible(self.elm_crateAccountError)
        return self.get_text(self.elm_crateAccountError)

