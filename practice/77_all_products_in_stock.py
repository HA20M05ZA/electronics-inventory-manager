import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)


def all_products_in_stock(products):
    result = all(product["stock"] != 0 for product in products)

    return result


result = all_products_in_stock(products)

print(result)
