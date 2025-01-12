from selenium.webdriver.common.by import By
from utilities.manage_pages import *
from utilities.ui_actions import UiActions



class LoginPage(UiActions):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.home_page = None

    # Locators
    txt_loginUsername = (By.NAME, "user-name")
    txt_password = (By.NAME, "password")
    btn_login = (By.ID, "login-button")
    elm_errorMassage = (By.XPATH, "//*[@data-test=\"error\"]")

    def login_action(self,  login_data):
        self.fill_action(self.txt_loginUsername, login_data["username"])
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
