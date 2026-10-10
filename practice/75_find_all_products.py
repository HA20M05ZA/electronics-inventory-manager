import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)


def find_all_products(products, search):
    select = []
    for product in products:
        if (
            search in product["name"].lower()
            or search in product["brand"].lower()
            or search in product["category"].lower()
        ):
            select.append(product)

    return select


search = input("Search: ").lower().strip()
result = find_all_products(products, search)

for product in result:
    print(f"{product['name']} - ${product['price']}")
