import requests

def main():
    base = input("Currency: ")
    res = requests.get("http://data.fixer.io/api/latest?access_key=5deecb6c00ede7c2ff33be1626d749cc",
                        params={"symbols":base})
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    data = res.json()
    rate = data["rates"][base]
    print(f"1 EUR is equal to {rate} {base}")

if __name__ == '__main__':
    main()
