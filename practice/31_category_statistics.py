import json
import sys

with open("../data/electronics.json", "r") as file:
    products = json.load(file)

category_type = input("Enter category: ").lower().strip()
items = 0
total = 0
select_product = []
found = False
for product in products:
    if product["category"] == category_type:
        items += 1
        total += product["price"]
        select_product.append(product)
        found = True
if not found:
    print("No products found for this category")
    sys.exit()

average = total / items
max_product = max(select_product, key=lambda product: product["price"])
min_product = min(select_product, key=lambda product: product["price"])

print(f"{category_type} Statistics")
print("-" * 20)
print(f"{'Product:' if items == 1 else 'Products:'} {items}")
print(f"Average price: ${average:.2f}")
print(f"Most expensive: {max_product['name']} - ${max_product['price']}")
print(f"Cheapest: {min_product['name']} - ${min_product['price']}")
