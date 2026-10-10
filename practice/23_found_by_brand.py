import json
import sys

with open("../data/electronics.json", "r") as file:
    products = json.load(file)

select_brand = input("Enter brand: ").lower()

brand = []
found = False
for product in products:
    if product["brand"].lower() == select_brand:
        brand.append(product)
        found = True


if not found:
    print("No products found for this brand.")
    sys.exit()

most_expensive = max(brand, key=lambda product: product["price"])


print(f"Most expensive {select_brand.title()} product")
print("-" * 25)
print(f"Product: {most_expensive['name']}")
print(f"Price: ${most_expensive['price']}")
