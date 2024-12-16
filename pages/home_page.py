from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from utilities.ui_actions import UiActions


class HomePage(UiActions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    img_logo = (By.CLASS_NAME, "logo")
    url_homePage = "https://magento.softwaretestingboard.com/"
    btn_singIn = (By.XPATH, "//a[contains(text(), 'Sign In')]")
    btn_create_user = (By.XPATH, "//a[contains(text(), 'Create an Account')]")
    elm_loggedIn = (By.CLASS_NAME, "logged-in")


    # Actions
    def navi_to_homepage(self):
        self.driver.get(self.url_homePage)

    def is_logo_displayed(self):
        return self.is_element_visible(self.img_logo)

    def navi_to_login(self):
        self.navi_to_homepage()
        self.click_action(self.btn_singIn)

    def navi_to_create_user(self):
        self.navi_to_homepage()
        self.click_action(self.btn_create_user)

    def get_user_name(self):
        self.wait_for_page_load()
        self.is_element_visible(self.elm_loggedIn)
        return self.get_text(self.elm_loggedIn)

    def verify_user_logged_in(self, name):
        self.wait_for_page_load()
        assert self.get_user_name() ==  f"Welcome, {name}!", "Login fails"