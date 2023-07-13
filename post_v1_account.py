import requests

def post_v1_account():
    """
    Register new user
    :return:
    """
    url = "http://localhost:5051/v1/account"

    payload = {
      "login": "lodin7599",
      "email": "lodin7599@mail.ru",
      "password": "lodin7599"
    }
    headers = {
      'X-Dm-Auth-Token': '<string>',
      'X-Dm-Bb-Render-Mode': '<string>',
      'Content-Type': 'application/json',
      'Accept': 'text/plain'
    }

    response = requests.request(
        method="POST",
        url=url,
        headers=headers,
        json=payload)
    return response

# post_v1_account()
response = post_v1_account()
print(response.content)
print(response.url)
print(response.status_code)
print(response.json()['type'])
print(response.json()['title'])

print(response.request.method)
print(response.request.url)
print(response.request.body)
print(response.request.headers)
print(response.request.hooks)




