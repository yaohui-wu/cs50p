import sys

import requests


def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    try:
        bitcoin_amount = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    # Replace "YourApiKey" with your CoinCap API key
    url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey"
    # Fetch current Bitcoin price data
    try:
        response = requests.get(url)
    except requests.RequestException:
        sys.exit("Failed to fetch Bitcoin price")
    o = response.json()
    price = float(o["data"]["priceUsd"])
    cost = price * bitcoin_amount
    print(f"${cost:,.4f}")


if __name__ == "__main__":
    main()
