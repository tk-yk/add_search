import requests
# zipcode = input("郵便番号は（ハイフンなし番号）>")
zipcode="0287111"
response = requests.get(f"https://zip-cloud.appspot.com/api/search?zipcode={zipcode}")
results=response.json()['results']
都道府県名=results[0]['address1']
市区町村名=results[0]['address2']
町域名=results[0]['address3']
address = f"{都道府県名}{市区町村名}{町域名}"


address = search_address(zipcode="028711")
print(address)

print(address)





