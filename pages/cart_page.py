from selenium.webdriver.common.by import By
from utilities.manage_pages import *
from utilities.ui_actions import UiActions
from selenium.webdriver.support.ui import WebDriverWait



class CartPage(UiActions):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.home_page = None

    # Locators
    btn_checkout = (By.LINK_TEXT, "CHECKOUT")
    txt_continue_shopping = (By.LINK_TEXT, "Continue Shopping")
    elm_cart_item = (By.CLASS_NAME, "cart_item")

    def continue_shopping(self):
        self.click_action(self.txt_continue_shopping)

    def checkout(self):
        self.click_action(self.btn_checkout)
