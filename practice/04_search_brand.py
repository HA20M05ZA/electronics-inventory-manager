import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)

print("--" * 20)

found = False
brand = input("Enter brand: ").lower()

for product in products:
    if brand == product["brand"].lower():
        print(f"{product['name']} - ${product['price']}")
        found = True

if not found:
    print("No products found for this brand.")
