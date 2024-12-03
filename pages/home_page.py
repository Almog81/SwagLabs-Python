from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.ui_actions import UiActions


class HomePage(UiActions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    img_logo = (By.CLASS_NAME, "logo.img-responsive")
    url_homePage = "http://www.automationpractice.pl/index.php"
    btn_singIn = (By.CLASS_NAME, "login")

    # Actions
    def navi_to_homepage(self):
        self.driver.get(self.url_homePage)

    def is_logo_displayed(self):
        return self.is_element_visible(self.img_logo)

    def navi_to_login(self):
        self.navi_to_homepage()
        self.click_action(self.btn_singIn)


