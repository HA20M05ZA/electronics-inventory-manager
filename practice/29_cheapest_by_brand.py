import json
import sys

with open("../data/electronics.json", "r") as file:
    products = json.load(file)

select_brand = input("Enter brand: ").lower()

found = False
brand = []
for product in products:
    if product["brand"].lower() == select_brand:
        brand.append(product)
        found = True
if not found:
    print("No products found for this brand.")
    sys.exit()
min_product = min(brand, key=lambda product: product["price"])

print(f"Cheapest {select_brand.capitalize()} product")
print("-" * 20)
print(f"Product: {min_product['name']}\nPrice: {min_product['price']}")
