from utilities.manage_pages import *

login_data_list = read_from_json("loginData.json")

class TestSanityScenarios:
    def test_login_page_logo(self, pages):
        pages.home_page.navi_to_homepage()
        assert pages.home_page.is_logo_displayed(), "Logo is not displayed"

    @pytest.mark.parametrize("login_data", login_data_list)
    def test_login_action(self, pages, login_data):
        pages.home_page.navi_to_homepage()
        pages.login_page.login_action(login_data)
