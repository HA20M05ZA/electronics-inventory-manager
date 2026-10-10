import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)


def get_product_names(products):
    names = []
    for product in products:
        names.append(product["name"])

    return names


result = get_product_names(products)

for product in result:
    print(f"{product}")
