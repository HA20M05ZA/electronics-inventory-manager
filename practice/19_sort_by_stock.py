import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)

products_sorted = sorted(products, key=lambda product: product["stock"], reverse=True)

print("Product sorted by stock")
print("-" * 25)

for product in products_sorted:
    print(f"{product['name']} - {product['stock']} available")
