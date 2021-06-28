import requests

url = "https://opentdb.com/api.php?amount=10&category=15&difficulty=easy&type=multiple"

resp= requests.get(url)

x= resp.json()

# print(x)

# print(type(x))

print(x["results"][0]["question"])

