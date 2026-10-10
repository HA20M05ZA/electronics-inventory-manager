import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)


def get_most_expensive_product(products):
    most_expensive = max(products, key=lambda product: product["price"])
    return most_expensive


result = get_most_expensive_product(products)
print(f"{result['name']} - ${result['price']}")
