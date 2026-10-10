import json
import sys

with open("../data/electronics.json", "r") as file:
    products = json.load(file)

stock_limit = int(input("Enter stock limit: "))

found = False
for product in products:
    if product["stock"] <= stock_limit and product["stock"] != 0:
        print(f"{product['name']} - {product['stock']} remaining")
        found = True

if not found:
    print("No low-stock products found.")
    sys.exit()
