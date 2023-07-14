import requests
from services.dm_api_account import DmApiAccount
def test_post_v1_account():
    api = DmApiAccount(host='http://localhost:5051')
    json = {"login": "lodin1209",
            "email": "lodin1209@mail.ru",
            "password": "lodin1209"}
    response = api.account.post_v1_account(
        json=json
    )
    print(response)


