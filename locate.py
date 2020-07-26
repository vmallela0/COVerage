import requests

res = requests.get("https://ipinfo.io/")
data = res.json()

# print(res.text)
# print(data)