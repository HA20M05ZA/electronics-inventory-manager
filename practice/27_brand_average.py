import json
import sys

with open("../data/electronics.json", "r") as file:
    products = json.load(file)

select_brand = input("Enter brand: ").lower()

total = 0
count = 0
found = False
for product in products:
    if product["brand"].lower() == select_brand:
        total += product["price"]
        count += 1
        found = True
if not found:
    print("No products found for this brand.")
    sys.exit()

average = total / count

print(total)
print(average)
