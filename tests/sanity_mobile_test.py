from utilities.common_ops_mobile import *
from utilities.manage_mobile_pages import *

login_data_list = read_from_json("loginData.json")

class TestSanityScenarios:
    @pytest.mark.parametrize("login_data", login_data_list)
    def test_01_login_all_type_of_users(self, pages, login_data):
        pages.login_page.login_all_users(login_data)

    def test_02_adding_lowest_to_cart(self,pages):
        pages.login_page.safe_login()
        pages.home_page.add_lowest_item_to_cart()