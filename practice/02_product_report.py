import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)

print("--" * 20)

for product in products:
    print(
        f"{product['name']} - {product['brand']} "
        f"- ${product['price']} - stock: {product['stock']}"
    )

print("--" * 20)
