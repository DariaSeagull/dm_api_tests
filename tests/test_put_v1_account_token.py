import requests

from services.dm_api_account import DmApiAccount


def test_put_v1_account_token():
    api = DmApiAccount(host='http://localhost:5051')
    token = 'cd1d618d-5b0e-43f3-84b0-6c344b9c02cb'
    response = api.account.put_v1_account_token(
        token=token
    )
    print(response)