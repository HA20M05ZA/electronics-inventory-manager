import json
import sys

with open("../data/electronics.json", "r") as file:
    products = json.load(file)

select_brand = input("Enter the brand: ").lower()
maximum_price = float(input("Enter maximum_price: "))
minimum_price = float(input("Enter minimum_price: "))

found = False
print(
    f"{select_brand.capitalize()} Products between ${minimum_price} and ${maximum_price}"
)
print("-" * 20)
for product in products:
    if (
        product["brand"].lower() == select_brand
        and product["price"] <= maximum_price
        and product["price"] >= minimum_price
    ):
        print(f"{product['name']} - ${product['price']}")
        found = True

if not found:
    print("No products found.")
    sys.exit()
