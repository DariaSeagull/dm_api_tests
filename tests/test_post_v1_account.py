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

    token = 'cd1d618d-5b0e-43f3-84b0-6c344b9c02cb'
    response = api.account.put_v1_account_token(
        token=token
    )
    print(response)



