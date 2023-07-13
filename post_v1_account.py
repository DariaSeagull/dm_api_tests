import requests



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




