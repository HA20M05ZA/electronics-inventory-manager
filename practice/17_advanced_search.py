import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)

brand = input("Enter brand: ").lower()
category = input("Enter category: ").lower()

print(f"Products matching {brand} + {category}")
print("-" * 20)
found = False
for product in products:
    if product["brand"].lower() == brand and product["category"].lower() == category:
        print(f"{product['name']} - ${product['price']}")
        found = True

if not found:
    print("No products found.")
