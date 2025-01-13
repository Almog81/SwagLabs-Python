from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from utilities.ui_actions import UiActions


class HomePage(UiActions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.login_page = None
        self.cart_page = None

    # Locators
    img_logo = (By.CLASS_NAME, "app_logo")
    url_homePage = "https://www.saucedemo.com/v1/index.html"
    btn_register = (By.XPATH, "//a[contains(text(), 'Register')]")

    elm_product_label = (By.CLASS_NAME, "product_label")
    img_inventory_item = (By.CLASS_NAME, "inventory_item_img")
    elm_cart = (By.CLASS_NAME, "shopping_cart_link")

    select_filter = (By.CLASS_NAME, "product_sort_container")
    btn_add_to_cart = (By.CLASS_NAME, "btn_inventory")

    # Actions
    def navi_to_homepage(self):
        self.driver.get(self.url_homePage)

    def is_logo_displayed(self):
        return self.is_element_visible(self.img_logo)

    def navi_to_cart(self):
        self.click_action(self.elm_cart)
        assert self.is_element_visible(self.cart_page.btn_checkout)

    def add_lowest_item_to_cart(self):
        self.drop_down_select(self.select_filter, "Price (low to high)")

        add_to_cart_buttons = self.driver.find_elements(*self.btn_add_to_cart)
        if add_to_cart_buttons:
            self.click_action(add_to_cart_buttons[0])
        else:
            raise Exception("No 'Add to cart' buttons found.")

        self.navi_to_cart()
        assert len(self.cart_page.elm_cart_item) > 0, "The cart is empty! No items were added."
