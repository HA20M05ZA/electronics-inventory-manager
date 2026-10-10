import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)


def filter_by_price(products, minimum_price, maximum_price):
    select = []
    for product in products:
        if product["price"] <= maximum_price and product["price"] >= minimum_price:
            select.append(product)
    return select


minimum = float(input("Minimum: "))
maximum = float(input("Maximum: "))
result = filter_by_price(products, minimum_price=minimum, maximum_price=maximum)
for product in result:
    print(f"{product['name']} - ${product['price']}")
