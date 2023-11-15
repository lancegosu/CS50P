import requests
import sys

if len(sys.argv) == 2:
    try:
        n = float(sys.argv[1])
    except:
        print("Command-line argument is not a number")
        sys.exit(1)
else:
    print("Missing command-line argument")
    sys.exit(1)

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = response.json()
    btc = o["bpi"]["USD"]["rate_float"]
    total = btc * n
    print(f"${total:,.4f}")
except requests.RequestException:
    print("RequestException")
    sys.exit(1)