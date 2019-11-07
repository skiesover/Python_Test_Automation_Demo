from tests.base_test import BaseTest
from utils.services import Services


# UI Test 1
# Create Default Alert and verify it is displayed un the list of alerts and verify shown details are proper
class CreateAlertAndVerifyDetails(BaseTest):
    test_alert = 'test_alert_1'

    def test(self):
        (Services()
         .navigate_to_alerts_web_path_tab()

         # precondition - delete alert if exists
         .delete_alert_by_name(self.test_alert)

         # test
         .create_new_default_alert(self.test_alert)
         .check_alert_details_by_name(self.test_alert)

         # after-method - delete created alert
         .delete_alert_by_name(self.test_alert))


# UI Test 2
# Delete existing alert and make sure it is not displayed in alerts list anymore
class DeleteExistingAlert(BaseTest):
    test_alert = 'test_alert_2'

    def test(self):
        (Services()
         .navigate_to_alerts_web_path_tab()

         # precondition - create new alert
         .create_new_default_alert(self.test_alert)

         # test
         .select_alert_by_name(self.test_alert)
         .click_delete_button()
         .check_delete_confirmation_displayed(self.test_alert)
         .click_ok_delete_button()
         .check_alert_not_displayed_in_list(self.test_alert))


# UI Test 3
# Edit existing alert and make sure changes are reflected
class EditExistingAlert(BaseTest):
    test_alert = 'test_alert_old'
    edited_test_alert = 'test_alert_edited'
    violates_value = 5
    clears_value = 8

    def test(self):
        (Services()
         .navigate_to_alerts_web_path_tab()

         # precondition - delete alert if exists and create new one
         .delete_alert_by_name(self.edited_test_alert)
         .create_new_default_alert(self.test_alert)

         # test
         .edit_alert_by_name(self.test_alert, self.edited_test_alert, self.violates_value, self.clears_value)
         .check_alert_not_displayed_in_list(self.test_alert)
         .check_alert_details_by_name(self.edited_test_alert, self.violates_value, self.clears_value)

         # after-method - delete updated alert
         .delete_alert_by_name(self.edited_test_alert))