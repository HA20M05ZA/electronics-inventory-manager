import json
import sys

with open("../data/electronics.json", "r") as file:
    products = json.load(file)


highest_price = float("-inf")
most_expensive = None
found = False


select = input("Enter brand: ").lower()
for product in products:
    if select == product["brand"].lower() and highest_price < product["price"]:
        highest_price = product["price"]
        most_expensive = product["name"]
        found = True

if not found:
    print("sorry but we don't have any brand with this name.")
    sys.exit()

print(f"Most expensive {select.title()} product")
print("-" * 20)
print(f"{most_expensive}\nPrice: ${highest_price}")
