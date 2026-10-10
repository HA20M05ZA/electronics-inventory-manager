import json
import sys

with open("../data/electronics.json", "r") as file:
    products = json.load(file)

select_brand = input("Enter brand: ").lower()

total = 0
count = 0
found = False
brand = []
for product in products:
    if product["brand"].lower() == select_brand:
        total += product["price"]
        count += 1
        found = True
        brand.append(product)
if not found:
    print("No products found for this brand.")
    sys.exit()

average = total / count
most_expensive = max(brand, key=lambda product: product["price"])

print(f"{select_brand.capitalize()} Statistics")
print("-" * 20)
print(f"products: {count}")
print(f"Average price: ${average:.2f}")
print(f"Most expensive: {most_expensive['name']} - ${most_expensive['price']}")
