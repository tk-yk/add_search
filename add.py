import requests


def search_address(zipcode):
    response = requests.get(f"https://zip-cloud.appspot.com/api/search?zipcode={zipcode}")

    results = response.json()['results']

    都道府県名 = results[0]['address1']
    市区町村名 = results[0]['address2']
    町域名 = results[0]['address3']

    address = f"{都道府県名}{市区町村名}{町域名}"
    return address


def main():
    zipcode = "0287111"

    address = search_address(zipcode)
    print(address)


# zipcode = input("郵便番号は（ハイフンなし番号）>")
if __name__ == '__main__':
    main()
