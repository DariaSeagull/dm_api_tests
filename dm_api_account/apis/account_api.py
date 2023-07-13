import requests
from requests import Response
from ..models.registration_model import registration_model
from ..models.reset_password_model import reset_password_model
from ..models.change_email_model import change_email_model
from ..models.change_password_model import change_password_model
class AccountApi:
    def __int__(self, host):
        self.host = host

    def post_v1_account(self, json: registration_model) -> Response:
        """
        :param json registration_model
        Register new user
        :return:
        """

        response = requests.request(
            method="POST",
            url=f"{self.host}/v1/account",
            json=json)
        return response

    def post_v1_account_password(self, json: reset_password_model) -> Response:
        """
        :param json reset_password_model
        Reset registered user password
        :return:
        """

        headers = {
            'X-Dm-Auth-Token': '<string>',
            'X-Dm-Bb-Render-Mode': '<string>',
            'Content-Type': 'application/json',
            'Accept': 'text/plain'
        }

        response = requests.request(
            method="POST",
            url=f"{self.host}/v1/account/password",
            headers=headers,
            json=json
        )
        return response

    def put_v1_account_email(self, json: change_email_model) -> Response:
        """
        :param json change_email_model
        Change registered user email
        :return:
        """
        headers = {
            'X-Dm-Auth-Token': '<string>',
            'X-Dm-Bb-Render-Mode': '<string>',
            'Content-Type': 'application/json',
            'Accept': 'text/plain'
        }

        response = requests.request(
            method="PUT",
            url=f"{self.host}/v1/account/email",
            headers=headers,
            json=json
        )
        return response

    def put_v1_account_password(self, json: change_password_model) -> Response:
        """
        :param json change_password_model
        Change registered user password
        :return:
        """

        headers = {
            'X-Dm-Auth-Token': '<string>',
            'X-Dm-Bb-Render-Mode': '<string>',
            'Content-Type': 'application/json',
            'Accept': 'text/plain'
        }

        response = requests.request(
            method="PUT",
            url=f"{self.host}/v1/account/password",
            headers=headers,
            json=json
        )
        return response

    def put_v1_account_token(self):
        """
        Activate registered user
        :return:
        """
        token = '23232'
        headers = {
            'X-Dm-Auth-Token': '<string>',
            'X-Dm-Bb-Render-Mode': '<string>',
            'Accept': 'text/plain'
        }

        response = requests.request(
            method="PUT",
            url=f"{self.host}/v1/account/{token}",
            headers=headers
        )
        return response

    def get_v1_account(self):
        """
        Get current user
        :return:
        """
        headers = {
            'X-Dm-Auth-Token': '<string>',
            'X-Dm-Bb-Render-Mode': '<string>',
            'Accept': 'text/plain'
        }

        response = requests.request(
            method="GET",
            url=f"{self.host}/v1/account",
            headers=headers)
        return response