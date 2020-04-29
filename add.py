import requests

response = requests.get("https://zip-cloud.appspot.com/api/search?zipcode=7830060")

print(response)
print(response.text)


