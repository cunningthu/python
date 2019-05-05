import requests

def main():
    res = requests.get("http://data.fixer.io/api/latest?access_key=5deecb6c00ede7c2ff33be1626d749cc&symbols=USD")
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    data = res.json()
    print(data)

if __name__ == "__main__":
    main()
