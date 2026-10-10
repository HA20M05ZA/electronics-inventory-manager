import json
import sys

with open("../data/electronics.json", "r") as file:
    products = json.load(file)

category = input("Enter category: ").lower()
minimum_price = float(input("Enter minimum price: "))
maximum_price = float(input("Enter maximum price: "))

print(f"{category.capitalize()} products Between ${minimum_price} and ${maximum_price}")
print("-" * 20)

items = 0
total = 0
select = []
found = False

for product in products:
    if (
        product["category"].lower() == category
        and product["price"] <= maximum_price
        and product["price"] >= minimum_price
    ):
        items += 1
        total += product["price"]
        select.append(product)
        print(f"{product['name']} - ${product['price']}")
        found = True

if not found:
    print("No products found in this category")
    sys.exit()

average = total / items
most_expensive = max(select, key=lambda product: product["price"])
cheapest = min(select, key=lambda product: product["price"])


print(f"\n{'Product:' if items == 1 else 'products:'} {items}")
print(f"Average price: ${average:.2f}")
print(f"Most expensive: {most_expensive['name']} - ${most_expensive['price']}")
print(f"Cheapest: {cheapest['name']} - ${cheapest['price']}")
