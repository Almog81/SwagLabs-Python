from selenium.webdriver.common.by import By
from utilities.manage_mobile_pages import *
from utilities.ui_actions import UiActions
from selenium.webdriver.support.ui import WebDriverWait



class CartPage(UiActions):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.home_page = None

    # Locators
    btn_checkout = (By.XPATH, "//*[@text=\"CHECKOUT\"]")
    txt_continue_shopping = (By.XPATH, "//*[@text=\"CONTINUE SHOPPING\"]")
    elm_cart_item = (By.XPATH, "//*[@content-desc=\"test-Item\"]")

    def continue_shopping(self):
        self.click_action(self.txt_continue_shopping)

    def checkout(self):
        self.click_action(self.btn_checkout)
