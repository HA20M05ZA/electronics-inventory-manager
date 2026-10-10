import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)

print("Products currently in stock")
print("-" * 20)


for product in products:
    if product["stock"] != 0:
        print(f"{product['name']} - {product['stock']} available")
