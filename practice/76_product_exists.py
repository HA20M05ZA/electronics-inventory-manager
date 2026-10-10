import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)


def product_exists(products, search):
    select = any(
        search in product["name"].lower()
        or search in product["brand"].lower()
        or search in product["category"].lower()
        for product in products
    )
    return select


search = input("Search: ").lower().strip()
result = product_exists(products, search)
print(result)
