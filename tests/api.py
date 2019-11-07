import requests
import unittest

from utils.api_services import ApiServices
from utils.global_constants import *


# API Test
# CREATE AND VERIFY ALERT USING API
class CreateAndCheckAlertUsingApi(unittest.TestCase):
    services = ApiServices()
    ALERT_NAME = 'test_alert_api_' + services.get_random_str()

    alert_id_from_response = ''
    alert_name_from_response = ''

    def test(self):
        # test
        self.create_alert()
        self.assert_alert_name()
        self.check_alert_is_created()

        # after-method (delete alert)
        self.delete_alert()

    # internal implementation is hidden below #
    def create_alert(self):
        create_alert_request = requests.post(self.services.get_alert_url(),
                                             data=self.services.get_create_alert_payload(self.ALERT_NAME),
                                             headers=self.services.get_create_alert_headers(),
                                             auth=(USER_ID, PASSWORD))

        self.alert_id_from_response = self.services.get_alert_id_from_response(create_alert_request.text)
        self.alert_name_from_response = self.services.get_alert_name_from_response(create_alert_request.text)
        assert create_alert_request.status_code == 200
        print('created alert name is: ' + self.alert_name_from_response)

    def assert_alert_name(self):
        assert self.alert_name_from_response == self.ALERT_NAME

    def check_alert_is_created(self):
        get_request = requests.get(self.services.get_alert_url(self.alert_id_from_response),
                                   auth=(USER_ID, PASSWORD))

        assert get_request.status_code == 200
        name = self.services.get_alert_name_from_response(get_request.text)
        assert name == self.ALERT_NAME

    def delete_alert(self):
        delete_request = requests.delete(self.services.get_alert_url(self.alert_id_from_response),
                                         auth=(USER_ID, PASSWORD))

        assert delete_request.status_code == 204