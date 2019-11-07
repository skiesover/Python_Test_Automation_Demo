from tests.base_test import BaseTest
from pages.pages import LoginPage, HomePage, ManageAlertProfilesPage
from utils.global_constants import *


# This class holds additional functions for UI tests
class Services:

    def login_to_appneta(self):
        self.navigate_to_appneta_login_page()
        LoginPage() \
            .enter_userid(USER_ID) \
            .enter_password(PASSWORD) \
            .click_login_button()

    def navigate_to_alerts_web_path_tab(self):
        self.login_to_appneta()

        HomePage() \
            .click_settings_icon() \
            .click_manage_alert_profiles_link()

        ManageAlertProfilesPage().click_web_path_tab()

        return ManageAlertProfilesPage()

    def navigate_to_appneta_login_page(self):
        BaseTest.driver.get(APP_NETA_HOME_URL)