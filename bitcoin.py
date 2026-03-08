import requests
import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument ")

    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=7af5cde025877ed9fd2242e3bc2f6682b04c97e2aceba040013b494c0f901168")
        data = response.json()
        price = float(data["data"]["priceUsd"])
    except requests.RequestException:
        sys.exit("Error fetching data")

    cost = n * price
    print(f"${cost:,.4f}")


if __name__ == "__main__":
    main()
