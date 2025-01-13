from utilities.manage_pages import *

login_data_list = read_from_json("loginData.json")

class TestSanityScenarios:
    def test_01_login_page_logo(self, pages):
        pages.home_page.navi_to_homepage()
        assert pages.home_page.is_logo_displayed(), "Logo is not displayed"

    @pytest.mark.parametrize("login_data", login_data_list)
    def test_02_login_all_type_of_users(self, pages, login_data):
        pages.home_page.navi_to_homepage()
        pages.login_page.login_all_users(login_data)

    def test_03_adding_lowest_to_cart(self,pages):
        pages.login_page.safe_login()
        pages.home_page.add_lowest_item_to_cart()
