from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from utilities.manage_mobile_pages import *
from utilities.ui_actions import UiActions
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage(UiActions):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.home_page = None

    # Locators
    txt_username = (AppiumBy.ACCESSIBILITY_ID, "test-Username")
    txt_password = (AppiumBy.ACCESSIBILITY_ID, "test-Password")
    btn_login = (AppiumBy.ACCESSIBILITY_ID, "test-LOGIN")
    elm_errorMassage = (AppiumBy.ACCESSIBILITY_ID, "test-Error message")


    def login_action(self,  login_data):
        self.fill_action(self.txt_username, login_data["username"])
        self.fill_action(self.txt_password,  login_data["password"])
        self.click_action(self.btn_login)

    def login_all_users(self, login_data):
        self.login_action(login_data)
        self.verify_user_logged_in(login_data["typeOfUser"])


    def verify_user_logged_in(self, type_of_user):
        self.wait_for_page_load()
        if type_of_user != "locked_out":
            assert self.is_element_visible(self.home_page.elm_product_label), f"Login failed: {self.get_text(self.elm_errorMassage)}"
            if type_of_user == "problem":
                broken_images = self.check_broken_images(self.home_page.img_inventory_item)
                assert broken_images, f"Broken images found: {len(broken_images)}"
            if type_of_user == "performance_glitch":
                load_time = self.get_page_load_time()
                max_load_time = 5
                assert load_time >= max_load_time, f"Page load time is too long: {load_time:.2f} seconds"
        if type_of_user == "locked_out":
            assert self.is_element_visible(self.elm_errorMassage), f"Login failed: {self.get_text(self.elm_errorMassage)}"

    def safe_login(self):
        self.login_action(read_from_json("loginData.json")[0])