import random
import string

from utils.global_constants import *


# This class holds additional functions for API tests
class ApiServices:

    def get_alert_url(self, alert_id=''):
        return APP_NETA_HOME_URL + API_ALERT_URL_PART + alert_id

    def get_create_alert_payload(self, alert_name):
        return "{\"id\":null,\"name\":\"" + alert_name + \
               "\",\"useAsDefault\":false,\"visible\":true,\"orgId\":3398," \
               "\"categoryType\":\"WebPath\",\"attribs\":[{\"id\":null,\"param\":\"Connectivity\"," \
               "\"scope\":\"Overall\",\"overInterval\":2,\"underInterval\":2,\"value\":0}],\"global\":false}"

    def get_create_alert_headers(self):
        return {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def get_alert_id_from_response(self, response):
        str = response.replace('{"id":', '')
        return str.split(',"name"')[0]

    def get_alert_name_from_response(self, response):
        str = response.split('"name":"')[1]
        return str.split('","useAsDefault"')[0]

    def get_random_str(self):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(5))