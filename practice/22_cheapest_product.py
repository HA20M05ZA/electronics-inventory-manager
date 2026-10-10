import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)

cheapest_product = min(products, key=lambda product: product["price"])

print("Cheapest product")
print("-" * 25)
print(f"Product: {cheapest_product['name']}")
print(f"Price: ${cheapest_product['price']}")
