import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)

highest_price = float("-inf")
most_expensive = None
for product in products:
    if product["price"] > highest_price:
        highest_price = product["price"]
        most_expensive = product["name"]

print(f"{most_expensive}: ${highest_price}")
