from utilities.manage_pages import *

create_data = read_from_json("crateUsers.json")

class TestSanityScenarios:
    def test_home_page_logo(self, pages):
        pages.home_page.navi_to_homepage()
        assert pages.home_page.is_logo_displayed(), "Logo is not displayed"

    def test_login_action(self, pages):
        login_data = read_from_json("loginData.json")
        pages.home_page.navi_to_login()
        pages.login_page.login_action(login_data["email"], login_data["password"])
        assert pages.login_page.get_user_name() == login_data["name"], "Login fails"

    @pytest.mark.parametrize("user_data", create_data)
    def test_create_user(self, pages, user_data):
        pages.home_page.navi_to_login()
        pages.create_user_page.create_user_action(user_data)
