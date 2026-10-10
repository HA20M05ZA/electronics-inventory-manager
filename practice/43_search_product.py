import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)

search = input("> ").lower()


def search_product(products, search):
    select = []
    for product in products:
        if (
            search in product["name"].lower()
            or search in product["category"].lower()
            or search in product["brand"].lower()
        ):
            select.append(product)
    return select


result = search_product(products, search)
for product in result:
    print(
        f"Product: {product['name']}\nBrand: {product['brand']}\nPrice: ${product['price']}\n"
    )
