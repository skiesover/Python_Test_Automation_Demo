from selenium.webdriver.common.by import By
from tests.base_test import BaseTest

driver = BaseTest.driver


# These classes hold element locators and functions for UI pages
class LoginPage:
    userid_field_element = (By.CSS_SELECTOR, '#username-input')
    password_field_element = (By.CSS_SELECTOR, '#login-form>input:nth-child(6)')
    login_button_element = (By.CSS_SELECTOR, '#login-button')

    def enter_userid(self, userid):
        driver.find_element(*self.userid_field_element).send_keys(userid)
        return self

    def enter_password(self, password):
        driver.find_element(*self.password_field_element).send_keys(password)
        return self

    def click_login_button(self):
        driver.find_element(*self.login_button_element).click()
        return HomePage()


class HomePage:
    settings_icon_element = (By.CSS_SELECTOR, '.appneta_icon_icons_cog-collapsed.appneta_icon_icons_main')
    user_area_element = (
        By.CSS_SELECTOR, '.appneta_userbadge_userbadge_userBadge.appneta_global_modules_hoverBackground')
    manage_alert_profiles_link_element = (By.CSS_SELECTOR,
                                          '#top-nav-container>div>div.appneta_usermenu_usermenu_userMenu>'
                                          'span.appneta_usermenu_usermenu_configMenu>span>div>div>div>div>'
                                          'div.tooltipmenu.rc-tooltip-inner>div>section:nth-child(5)>ul>li:nth-child(1)>a')

    def click_settings_icon(self):
        driver.find_element(*self.settings_icon_element).click()
        return self

    def click_manage_alert_profiles_link(self):
        driver.find_element(*self.manage_alert_profiles_link_element).click()
        return ManageAlertProfilesPage()


class ManageAlertProfilesPage:
    web_path_tab_element = (By.CSS_SELECTOR, '#sqdCategory>button:nth-child(2)')
    new_button_element = (By.CSS_SELECTOR, 'button#addSQDButton')
    delete_button_element = (By.CSS_SELECTOR, '#deleteSQDButton')
    edit_button_element = (By.CSS_SELECTOR, '#editSQDButton')
    copy_button_element = (By.CSS_SELECTOR, '#copySQDButton')
    confirm_delete_text_element = (By.CSS_SELECTOR, '#appneta-pvc-confirm-dialog>div.msg')
    ok_delete_button_element = (By.CSS_SELECTOR, '.ui-button-primary>span.ui-button-text')
    alert_name_text_element = (By.CSS_SELECTOR, '#sqdTemplateNameRow')
    violates_text_element = (By.CSS_SELECTOR, '#connectivityValue')
    clears_text_element = (By.CSS_SELECTOR, '#connectivityClearValue')

    def click_web_path_tab(self):
        driver.find_element(*self.web_path_tab_element).click()
        return self

    def click_new_button(self):
        driver.find_element(*self.new_button_element).click()
        return NewOrEditAlertBlock()

    def click_delete_button(self):
        driver.find_element(*self.delete_button_element).click()
        return self

    def click_edit_button(self):
        driver.find_element(*self.edit_button_element).click()
        return NewOrEditAlertBlock()

    def check_delete_confirmation_displayed(self, alert_name):
        confirmation_text = driver.find_element(*self.confirm_delete_text_element).text
        expected_text = 'Are you sure you want to delete "' + alert_name + '"?'
        assert confirmation_text == expected_text
        return self

    def click_ok_delete_button(self):
        driver.find_element(*self.ok_delete_button_element).click()
        return self

    def check_alert_not_displayed_in_list(self, alert_name):
        elements = driver.find_elements(By.XPATH, '//optgroup//*[contains(text(), \'' + alert_name + '\')]')
        assert len(elements) == 0
        return self

    def create_new_default_alert(self, alert_name):
        try:
            if self.check_alert_not_displayed_in_list(alert_name):
                self \
                    .click_new_button() \
                    .enter_alert_name(alert_name) \
                    .click_add_condition_button() \
                    .click_create_button()
        except:
            print("Alert already exists.")

        return ManageAlertProfilesPage()

    def select_alert_by_name(self, alert_name):
        driver.implicitly_wait(1)
        self.get_alert_by_name(alert_name).click()
        return self

    def get_alert_by_name(self, alert_name):
        return driver.find_element(By.XPATH, '//optgroup//*[contains(text(), \'' + alert_name + '\')]')

    def delete_alert_by_name(self, alert_name):
        try:
            if self.get_alert_by_name(alert_name).is_displayed():
                self \
                    .select_alert_by_name(alert_name) \
                    .click_delete_button() \
                    .click_ok_delete_button()
        except:
            print("Element is not present.")
        return self

    def check_alert_details_by_name(self, alert_name, violates_value=2, clears_value=2):
        self.select_alert_by_name(alert_name)

        element_text = driver.find_element(*self.alert_name_text_element).text
        violates_text = driver.find_element(*self.violates_text_element).text
        clears_text = driver.find_element(*self.clears_text_element).text

        assert element_text == 'Alert Conditions for ' + alert_name + '.'
        assert violates_text == 'violates when connectivity lost for ' + str(violates_value) + ' consecutive tests'
        assert clears_text == 'clears after restored for ' + str(clears_value) + ' consecutive tests'

        return self

    def edit_alert_by_name(self, alert_name, updated_name, violates_value, clears_value):
        self \
            .select_alert_by_name(alert_name) \
            .click_edit_button() \
            .enter_alert_name(updated_name) \
            .fill_violates_field_with_value(violates_value) \
            .fill_clears_field_with_value(clears_value) \
            .click_add_condition_button() \
            .click_create_button()

        return self


class NewOrEditAlertBlock:
    alert_name_field_element = (By.CSS_SELECTOR, '.appneta_alert-profile-creator_alert-profile-creator_leftPanel>input')
    add_replace_condition_button_element = (By.CSS_SELECTOR, '.ui-button.ui-button-success')
    create_update_button_element = (By.CSS_SELECTOR, '.ui-button.ui-button-primary')
    violates_field_element = (By.CSS_SELECTOR, 'tr:nth-child(2)>td:nth-child(2)>div>span:nth-child(2)>input[type=number]')
    clears_field_element = (By.CSS_SELECTOR, 'tr:nth-child(3)>td:nth-child(2)>div>span:nth-child(2)>input[type=number]')

    def enter_alert_name(self, alert_name):
        alert_name_field = driver.find_element(*self.alert_name_field_element)
        alert_name_field.clear()
        alert_name_field.send_keys(alert_name)
        return self

    # this method should be called if Replace Conditions button needs to be clicked as well
    def click_add_condition_button(self):
        driver.find_element(*self.add_replace_condition_button_element).click()
        return self

    def fill_violates_field_with_value(self, value):
        violates_field = driver.find_element(*self.violates_field_element)
        violates_field.clear()
        violates_field.send_keys(value)
        return self

    def fill_clears_field_with_value(self, value):
        clears_field = driver.find_element(*self.clears_field_element)
        # for some reason clearing field directly doesn't work.
        # that's why temporary workaround is implemented to enter random value first
        clears_field.send_keys(1)
        clears_field.clear()
        clears_field.send_keys(value)
        return self

    # this method should be called if Update button needs to be clicked as well
    def click_create_button(self):
        driver.find_element(*self.create_update_button_element).click()
        return ManageAlertProfilesPage()