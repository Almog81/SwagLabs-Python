from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from utilities.ui_actions import UiActions


class HomePage(UiActions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.login_page = None

    # Locators
    img_logo = (By.CLASS_NAME, "app_logo")
    url_homePage = "https://www.saucedemo.com/v1/index.html"
    btn_register = (By.XPATH, "//a[contains(text(), 'Register')]")

    elm_product_label = (By.CLASS_NAME, "product_label")
    img_inventory_item = (By.CLASS_NAME, "inventory_item_img")

    # Actions
    def navi_to_homepage(self):
        self.driver.get(self.url_homePage)

    def is_logo_displayed(self):
        return self.is_element_visible(self.img_logo)

