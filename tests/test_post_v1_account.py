import requests
from services.dm_api_account import DmApiAccount
def test_post_v1_account():
    api = DmApiAccount(host='http://localhost:5051')
    json = {"login": "lodin7599",
            "email": "lodin7599@mail.ru",
            "password": "lodin7599"}
    response = api.account.post_v1_account(
        json=json
    )
    print(response)


