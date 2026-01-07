"""
Part 3: Dynamic Queries with User Input
=======================================
Difficulty: Intermediate
"""

import requests


# -------------------------------
# Exercise 3 solution:
# Input validation function
# -------------------------------
def get_valid_user_id(prompt):
    user_id = input(prompt)
    if not user_id.isdigit():
        print("❌ Please enter a valid number!")
        return None
    return user_id


def get_user_info():
    print("=== User Information Lookup ===\n")

    user_id = get_valid_user_id("Enter user ID (1-10): ")
    if not user_id:
        return

    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)

    if response.status_code == 200 and response.json() != {}:
        data = response.json()
        print(f"\n--- User #{user_id} Info ---")
        print(f"Name: {data['name']}")
        print(f"Email: {data['email']}")
        print(f"Phone: {data['phone']}")
        print(f"Website: {data['website']}")
    else:
        print(f"\nUser with ID {user_id} not found!")


def search_posts():
    print("\n=== Post Search ===\n")

    user_id = get_valid_user_id("Enter user ID to see their posts (1-10): ")
    if not user_id:
        return

    url = "https://jsonplaceholder.typicode.com/posts"
    params = {"userId": user_id}

    response = requests.get(url, params=params)
    posts = response.json()

    if posts:
        print(f"\n--- Posts by User #{user_id} ---")
        for i, post in enumerate(posts, 1):
            print(f"{i}. {post['title']}")
    else:
        print("No posts found for this user.")


def get_crypto_price():
    print("\n=== Cryptocurrency Price Checker ===\n")

    print("Available coins: btc-bitcoin, eth-ethereum, doge-dogecoin")
    coin_id = input("Enter coin ID: ").lower().strip()

    url = f"https://api.coinpaprika.com/v1/tickers/{coin_id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        price = data['quotes']['USD']['price']
        change = data['quotes']['USD']['percent_change_24h']

        print(f"\n--- {data['name']} ({data['symbol']}) ---")
        print(f"Price: ${price:,.2f}")
        print(f"24h Change: {change:+.2f}%")
    else:
        print("Coin not found!")


# -------------------------------
# Exercise 1 solution:
# Weather function
# -------------------------------
def get_weather():
    print("\n=== Weather Checker ===\n")

    cities = {
        "delhi": (28.61, 77.23),
        "mumbai": (19.07, 72.87),
        "pune": (18.52, 73.85),
        "bangalore": (12.97, 77.59)
    }

    city = input("Enter city: ").lower()

    if city not in cities:
        print("City not supported!")
        return

    lat, lon = cities[city]
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather = data["current_weather"]
        print(f"\nWeather in {city.title()}")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Wind Speed: {weather['windspeed']} km/h")
    else:
        print("Weather data not available.")


# -------------------------------
# Exercise 2 solution:
# Search todos by status
# -------------------------------
def search_todos():
    print("\n=== Todo Search ===\n")

    status = input("Show completed todos? (yes/no): ").lower()

    if status == "yes":
        completed = "true"
    elif status == "no":
        completed = "false"
    else:
        print("Invalid choice!")
        return

    url = "https://jsonplaceholder.typicode.com/todos"
    params = {"completed": completed}

    response = requests.get(url, params=params)
    todos = response.json()

    print(f"\nTodos (completed = {completed})")
    for todo in todos[:10]:
        print(f"- {todo['title']}")


def main():
    print("=" * 40)
    print("  Dynamic API Query Demo")
    print("=" * 40)

    while True:
        print("\nChoose an option:")
        print("1. Look up user info")
        print("2. Search posts by user")
        print("3. Check crypto price")
        print("4. Check weather")
        print("5. Search todos")
        print("6. Exit")

        choice = input("\nEnter choice (1-6): ")

        if choice == "1":
            get_user_info()
        elif choice == "2":
            search_posts()
        elif choice == "3":
            get_crypto_price()
        elif choice == "4":
            get_weather()
        elif choice == "5":
            search_todos()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()


# --- EXERCISES ---
#
# Exercise 1: Add a function to fetch weather for a city
# Use Open-Meteo API (no key required):
# https://api.open-meteo.com/v1/forecast?latitude=28.61&longitude=77.23&current_weather=true
# Challenge: Let user input city name (you'll need to find lat/long)
#
# Exercise 2: Add a function to search todos by completion status
# URL: https://jsonplaceholder.typicode.com/todos
# Params: completed=true or completed=false
#
# Exercise 3: Add input validation (check if user_id is a number)
