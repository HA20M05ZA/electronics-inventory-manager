import json
import sys

with open("../data/electronics.json", "r") as file:
    products = json.load(file)

brand = input("Enter brand: ").lower().strip()
category = input("Enter category: ").lower().strip()
count = 0
inventory_value = 0
total_price = 0
found = False

for product in products:
    if product["category"].lower() == category and product["brand"].lower() == brand:
        inventory_value += product["price"] * product["stock"]
        total_price += product["price"]
        count += 1
        found = True

if not found:
    print("No products found for this brand and category. ")
    sys.exit()

average_price = total_price / count

print(f"{category.capitalize()} - {brand.capitalize()} Inventory")
print("-" * 20)
print(f"{'Product:' if count == 1 else 'products:'} {count}")
print(f"Average price: ${average_price:.2f}")
print(f"Total inventory value: ${inventory_value}")
