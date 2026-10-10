import json
import sys

with open("../data/electronics.json", "r") as file:
    products = json.load(file)

brand = input("Enter brand: ").lower().strip()
total_value = 0
count = 0
found = False

for product in products:
    if product["brand"].lower() == brand:
        total_value += product["price"] * product["stock"]
        count += 1
        found = True

if not found:
    print("No products found for this brand.")
    sys.exit()

print(f"{brand.capitalize()} Inventory ")
print("-" * 20)
print(f"{'Product:' if count == 1 else 'products:'} {count}")
print(f"Total inventory value: ${total_value}")
