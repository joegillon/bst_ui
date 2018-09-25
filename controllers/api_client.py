import requests
import json


class ApiClient(object):

    headers = {
        'Content-type': 'application/json',
        'Accept': 'application/json'
    }

    @staticmethod
    def get(url):
        response = requests.get(url, headers=ApiClient.headers)
        if response.status_code in [200, 304]:
            return json.loads(response.content)
        print('Error: ', response.status_code)
