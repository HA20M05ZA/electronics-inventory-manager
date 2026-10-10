import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)


def calculate_inventory_value(price, stock):
    total = price * stock
    return total


for product in products:
    value = calculate_inventory_value(price=product["price"], stock=product["stock"])
    print(f"{product['name']} - ${value}")
