import requests
import sys
import json


def main():
    if len(sys.argv) == 1:
        return print("Missing command-line argument")
    try:
        n = float(sys.argv[1])
    except ValueError:
        return print("Command-line argument is not a number")
    try:
        bitcoin = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        return "Error"
    information = bitcoin.json()
    USD = information.get("bpi")
    list = USD.get("USD")
    value = list.get("rate_float")
    print(value)
    amount = n * value
    print(f"${amount:,.4f}")


main()
