import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)


def get_cheapest_product(products):
    cheapest = min(products, key=lambda product: product["price"])
    return cheapest


result = get_cheapest_product(products)
print("Cheapest product")
print("-" * 20)
print(f"Product: {result['name']}\nPrice: ${result['price']}")
