import requests
import sys

from endpoints.gcloud import Google


class Requests:
    @staticmethod
    def check_request(response, failure_message):
        if response.status_code not in [200, 201, 202, 204]:
            sys.exit(f'{response.status_code}, {failure_message}\n{response.content}')
        else:
            return response


class Terra(Requests):
    ROOT = 'https://api.firecloud.org/api'

    @classmethod
    def generate_headers(cls):
        token = Google.get_token()
        return {'Authorization': 'Bearer {}'.format(token)}

    @classmethod
    def get_all_workspaces(cls, headers):
        request = f'{cls.ROOT}/workspaces'
        response = cls.get_request(request, headers)
        return cls.check_request(response, 'failed to get workspaces from /workspaces endpoint')

    @staticmethod
    def get_request(request, headers):
        return requests.get(request, headers=headers)

    @classmethod
    def request(cls, request_function, format_function, **kwargs):
        headers = cls.generate_headers()
        response = request_function(headers, **kwargs)
        return format_function(response)
