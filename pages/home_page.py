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
    url_homePage = "https://parabank.parasoft.com/"
    btn_register = (By.XPATH, "//a[contains(text(), 'Register')]")
    elm_welcome = (By.XPATH, "//*[contains(text(), 'Welcome')]")
    elm_errorMassage = (By.CLASS_NAME, "error")


    # Actions
    def navi_to_homepage(self):
        self.driver.get(self.url_homePage)

    def is_logo_displayed(self):
        return self.is_element_visible(self.img_logo)

    def navi_to_create_user(self):
        self.navi_to_homepage()
        self.click_action(self.btn_register)

    def get_user_name(self):
        self.is_element_visible(self.elm_welcome)
        return self.get_text(self.elm_welcome)


    def verify_user_logged_in(self):
        self.wait_for_page_load()
        assert self.is_element_visible(self.elm_welcome), f"Login failed: {self.get_text(self.elm_errorMassage)}"
