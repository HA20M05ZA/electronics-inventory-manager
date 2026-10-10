import json
import sys

with open("../data/electronics.json", "r") as file:
    products = json.load(file)

min_price = float(input("Enter minimum price: "))
max_price = float(input("Enter maximum price: "))

found_products = []

found = False

for product in products:
    if product["price"] >= min_price and product["price"] <= max_price:
        found_products.append(f"{product['name']} - ${product['price']}")
        found = True

if not found:
    print("No products found in this price range.")
    sys.exit()

print(f"Products between ${min_price} and ${max_price}")
print("-" * 20)
for product in found_products:
    print(product)
