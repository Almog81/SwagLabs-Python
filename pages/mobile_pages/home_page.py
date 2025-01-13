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

    elm_product_label = (By.XPATH, "//*[@text=\"PRODUCTS\"]")
    img_inventory_item = (By.CLASS_NAME, "android.widget.ImageView")
    elm_cart = (By.XPATH, "//*[@content-desc=\"test-Cart\"]")

    select_filter = (By.XPATH, "//*[@content-desc=\"test-Modal Selector Button\"]")
    btn_add_to_cart = (By.XPATH, "(//*[@text=\"ADD TO CART\"])")

    btn_menu = (By.XPATH, "//*[@content-desc=\"test-Menu\"]")
    btn_logout = (By.XPATH, "//*[@content-desc=\"test-LOGOUT\"]")

    # Actions
    def is_logo_displayed(self):
        return self.is_element_visible(self.img_logo)

    def navi_to_cart(self):
        self.click_action(self.elm_cart)
        assert self.is_element_visible(self.cart_page.btn_checkout)

    def add_lowest_item_to_cart(self):
        self.drop_down_select(self.select_filter, "Price (low to high)")
        add_to_cart_buttons = self.get_elements_by_locator(self.btn_add_to_cart)
        if add_to_cart_buttons:
            self.click_action(add_to_cart_buttons[0])
        else:
            raise Exception("No 'Add to cart' buttons found.")

        self.navi_to_cart()
        assert len(self.cart_page.elm_cart_item) > 0, "The cart is empty! No items were added."
