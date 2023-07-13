import requests
from requests import Response
from ..models.login_credentials_model import login_credentials_model

class LoginApi:
    def __int__(self, host):
        self.host = host

    def post_v1_account_login(self, json: login_credentials_model) -> Response:
        """
        :param json login_credentials_model
        Authenticate via credentials
        :return:
        """
        headers = {
            'X-Dm-Bb-Render-Mode': '<string>',
            'Content-Type': 'application/json',
            'Accept': 'text/plain'
        }

        response = requests.request(
            method="POST",
            url=f"{self.host}/v1/account/login",
            headers=headers,
            json=json
        )
        return response

    def delete_v1_account_login(self):
        """
        Logout as current user
        :return:
        """
        headers = {
            'X-Dm-Auth-Token': '<string>',
            'X-Dm-Bb-Render-Mode': '<string>',
            'Accept': 'text/plain'
        }

        response = requests.request(
            method="DELETE",
            url=f"{self.host}/v1/account/login",
            headers=headers
        )
        return response

    def delete_v1_account_login_all(self):
        """
        Logout from every device
        :return:
        """
        headers = {
            'X-Dm-Auth-Token': '<string>',
            'X-Dm-Bb-Render-Mode': '<string>',
            'Accept': 'text/plain'
        }

        response = requests.request(
            method="DELETE",
            url=f"{self.host}/v1/account/login/all",
            headers=headers
        )
        return response