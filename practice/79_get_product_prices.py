import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)


def get_product_prices(products):
    prices = []
    for product in products:
        prices.append(product["price"])

    return prices


result = get_product_prices(products)
for price in result:
    print(f"${price}")
