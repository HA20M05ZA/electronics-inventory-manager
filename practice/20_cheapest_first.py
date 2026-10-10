import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)

products_sorted = sorted(products, key=lambda product: product["price"])

print("Products from cheapest to most expensive")
print("-" * 25)
for product in products_sorted:
    print(f"{product['name']} - ${product['price']}")
