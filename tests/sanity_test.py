from common_ops import home_page, login_page


class TestSanityScenarios:
    def test_home_page_logo(self):
        """Verify logo is displayed on home page"""
        assert home_page.is_logo_displayed(), "Logo is not displayed"

    def test_welcome_message(self):
        """Verify welcome message"""
        welcome_text = home_page.get_welcome_message()
        assert "Welcome" in welcome_text, "Unexpected welcome message"

    def test_login_functionality(self, driver):
        """Example of login functionality test"""
        # Navigate to home page if needed
        home_page.navi_to_homepage()

        # Perform login
        login_page.login_action("test_user", "password")

        # Verify login
        current_url = driver.current_url
        assert "/dashboard" in current_url, "Login failed"