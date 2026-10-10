import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)


def get_product_stock(products):
    stock = []
    for product in products:
        stock.append(product["stock"])

    return stock


result = get_product_stock(products)
for stock in result:
    print(f"{stock}")
