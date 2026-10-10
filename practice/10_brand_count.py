import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)

print("Product count by brand")
print("-" * 20)

brand_counts = {}

for product in products:
    if product["brand"] not in brand_counts:
        brand_counts[product["brand"]] = 1
    else:
        brand_counts[product["brand"]] += 1

print(brand_counts)
