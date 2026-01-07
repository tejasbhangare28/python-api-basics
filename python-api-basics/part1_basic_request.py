"""
Part 1: Basic GET Request
=========================
Difficulty: Beginner

Learn: How to make a simple GET request and view the response.

We'll use JSONPlaceholder - a free fake API for testing.
"""

import requests

# ---------------------------
# Exercise 1: Fetch post #5
# ---------------------------

# Step 1: Define the API URL
url = "https://jsonplaceholder.typicode.com/posts/5"

# Step 2: Make a GET request
response = requests.get(url)

# Step 3: Print the response
print("=== Exercise 1: Fetch Post #5 ===\n")
print(f"URL: {url}")
print(f"Status Code: {response.status_code}")
print(f"\nResponse Data:")
print(response.json())


# ---------------------------
# Exercise 2: Fetch all users
# ---------------------------

# Step 1: Define the API URL
url = "https://jsonplaceholder.typicode.com/users"

# Step 2: Make a GET request
response = requests.get(url)

# Step 3: Print the response
print("\n=== Exercise 2: Fetch All Users ===\n")
print(f"URL: {url}")
print(f"Status Code: {response.status_code}")
print(f"\nResponse Data:")
print(response.json())


# ------------------------------------------------
# Exercise 3: Fetch a post that doesn't exist
# ------------------------------------------------

# Step 1: Define the API URL
url = "https://jsonplaceholder.typicode.com/posts/999"

# Step 2: Make a GET request
response = requests.get(url)

# Step 3: Print the response
print("\n=== Exercise 3: Fetch Non-Existing Post ===\n")
print(f"URL: {url}")
print(f"Status Code: {response.status_code}")
print(f"\nResponse Data:")
print(response.json())

