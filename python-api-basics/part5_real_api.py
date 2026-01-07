"""
Part 5: Real-World APIs - Weather & Crypto Dashboard
====================================================
Difficulty: Advanced
"""

import requests
from datetime import datetime
import json
import os

# -------------------------------
# Exercise 1: Added more cities
# -------------------------------
CITIES = {
    "delhi": (28.6139, 77.2090),
    "mumbai": (19.0760, 72.8777),
    "bangalore": (12.9716, 77.5946),
    "chennai": (13.0827, 80.2707),
    "kolkata": (22.5726, 88.3639),
    "hyderabad": (17.3850, 78.4867),
    "pune": (18.5204, 73.8567),
    "jaipur": (26.9124, 75.7873),
    "new york": (40.7128, -74.0060),
    "london": (51.5074, -0.1278),
    "tokyo": (35.6762, 139.6503),
    "sydney": (-33.8688, 151.2093),
}

CRYPTO_IDS = {
    "bitcoin": "btc-bitcoin",
    "ethereum": "eth-ethereum",
    "dogecoin": "doge-dogecoin",
    "cardano": "ada-cardano",
    "solana": "sol-solana",
    "ripple": "xrp-xrp",
}


# -------------------------------
# WEATHER
# -------------------------------
def get_weather(city_name):
    city_lower = city_name.lower().strip()

    if city_lower not in CITIES:
        print(f"\nCity '{city_name}' not found.")
        return None

    lat, lon = CITIES[city_lower]

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True,
        "timezone": "auto"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching weather: {e}")
        return None


def display_weather(city_name):
    data = get_weather(city_name)
    if not data:
        return

    current = data["current_weather"]

    print(f"\n{'=' * 40}")
    print(f"  Weather in {city_name.title()}")
    print(f"{'=' * 40}")
    print(f"  Temperature: {current['temperature']}°C")
    print(f"  Wind Speed: {current['windspeed']} km/h")
    print(f"{'=' * 40}")


# -------------------------------
# CRYPTO
# -------------------------------
def get_crypto_price(coin_name):
    coin_lower = coin_name.lower().strip()
    coin_id = CRYPTO_IDS.get(coin_lower, coin_lower)

    url = f"https://api.coinpaprika.com/v1/tickers/{coin_id}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        return None


def display_crypto(coin_name):
    data = get_crypto_price(coin_name)

    if not data:
        print("Coin not found.")
        return

    usd = data["quotes"]["USD"]

    print(f"\n{'=' * 40}")
    print(f"  {data['name']} ({data['symbol']})")
    print(f"{'=' * 40}")
    print(f"  Price: ${usd['price']:,.2f}")
    print(f"  24h Change: {usd['percent_change_24h']:+.2f}%")
    print(f"{'=' * 40}")


# ------------------------------------------------
# Exercise 2: Compare multiple crypto prices
# ------------------------------------------------
def compare_cryptos(coins):
    print(f"\n{'=' * 55}")
    print(f"  Crypto Price Comparison")
    print(f"{'=' * 55}")
    print(f"  {'Name':<15}{'Price (USD)':<15}{'24h Change'}")
    print(f"  {'-' * 50}")

    results = []

    for coin in coins:
        data = get_crypto_price(coin)
        if data:
            usd = data["quotes"]["USD"]
            print(f"  {data['name']:<15}${usd['price']:<14,.2f}{usd['percent_change_24h']:+.2f}%")
            results.append({
                "name": data["name"],
                "price": usd["price"],
                "change_24h": usd["percent_change_24h"]
            })

    return results


# ------------------------------------------------
# Exercise 3: POST request example
# ------------------------------------------------
def create_post():
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {"title": "My Post", "body": "Content", "userId": 1}

    response = requests.post(url, json=payload)
    print("\nPost Created!")
    print(response.json())
    return response.json()


# ------------------------------------------------
# Exercise 4: Save results to JSON file
# ------------------------------------------------
def save_to_file(data, filename="results.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
    print(f"\nData saved to {filename}")


# ------------------------------------------------
# Exercise 5: API key support (OpenWeatherMap)
# ------------------------------------------------
def get_weather_with_api_key(city):
    api_key = os.environ.get("OPENWEATHER_API_KEY")

    if not api_key:
        print("No API key found. Using Open-Meteo instead.")
        return get_weather(city)

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"API Error: {e}")
        return None


# -------------------------------
# DASHBOARD
# -------------------------------
def dashboard():
    print("\n" + "=" * 50)
    print("   Real-World API Dashboard")
    print("=" * 50)

    while True:
        print("\nOptions:")
        print("  1. Check Weather")
        print("  2. Check Crypto Price")
        print("  3. Compare Cryptos")
        print("  4. Create Sample POST")
        print("  5. Exit")

        choice = input("\nSelect (1-5): ").strip()

        if choice == "1":
            print(f"Available: {', '.join(CITIES.keys())}")
            city = input("Enter city: ")
            display_weather(city)

        elif choice == "2":
            print(f"Available: {', '.join(CRYPTO_IDS.keys())}")
            coin = input("Enter crypto: ")
            display_crypto(coin)

        elif choice == "3":
            coins = input("Enter coins (comma separated): ").split(",")
            results = compare_cryptos([c.strip() for c in coins])
            save = input("Save results to file? (y/n): ").lower()
            if save == "y":
                save_to_file(results)

        elif choice == "4":
            post_data = create_post()
            save_to_file(post_data, "post_result.json")

        elif choice == "5":
            print("Goodbye! Happy coding!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    dashboard()


# --- CHALLENGE EXERCISES ---
#
# Exercise 1: Add more cities to the CITIES dictionary
#             Find coordinates at: https://www.latlong.net/
#
# Exercise 2: Create a function that compares prices of multiple cryptos
#             Display them in a formatted table
#
# Exercise 3: Add POST request example
#             Use: https://jsonplaceholder.typicode.com/posts
#             Send: requests.post(url, json={"title": "My Post", "body": "Content"})
#
# Exercise 4: Save results to a JSON file
#             import json
#             with open("results.json", "w") as f:
#                 json.dump(data, f, indent=2)
#
# Exercise 5: Add API key support for OpenWeatherMap
#             Sign up at: https://openweathermap.org/api
#             Use environment variables:
#             import os
#             api_key = os.environ.get("OPENWEATHER_API_KEY")
