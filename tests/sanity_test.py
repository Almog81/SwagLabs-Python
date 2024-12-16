from utilities.manage_pages import *

create_data = read_from_json("crateUsers.json")
login_data_list = read_from_json("loginData.json")

class TestSanityScenarios:
    def test_home_page_logo(self, pages):
        pages.home_page.navi_to_homepage()
        assert pages.home_page.is_logo_displayed(), "Logo is not displayed"

    @pytest.mark.parametrize("login_data", login_data_list)
    def test_login_action(self, pages, login_data):
        pages.home_page.navi_to_login()
        pages.login_page.login_action(login_data["email"], login_data["password"])
        pages.home_page.verify_user_logged_in(login_data["name"])

    @pytest.mark.parametrize("user_data", create_data)
    def test_create_user(self, pages, user_data):
        pages.home_page.navi_to_create_user()
        pages.create_user_page.create_user_action(user_data)
        pages.create_user_page.verify_user_created()
