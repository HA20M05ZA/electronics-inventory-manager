import json
import sys

with open("../data/electronics.json", "r") as file:
    products = json.load(file)

search = input("> ").lower()

select = []
found = False
for product in products:
    if (
        search in product["name"].lower()
        or search in product["category"].lower()
        or search in product["brand"].lower()
    ):
        select.append(product)
        found = True
if not found:
    print("No products found.")
    sys.exit()

for product in select:
    print(f"Product: {product['name']}")
    print(f"Brand: {product['brand']}")
    print(f"Category: {product['category']}")
    print(f"Price: ${product['price']}")
    print(f"Stock: {product['stock']}\n")
