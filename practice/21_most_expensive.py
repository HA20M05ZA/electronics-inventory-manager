import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)

most_expensive = max(products, key=lambda product: product["price"])

print("Most expensive product")
print("-" * 25)


print(f"Product: {most_expensive['name']}")
print(f"Price: ${most_expensive['price']}")
