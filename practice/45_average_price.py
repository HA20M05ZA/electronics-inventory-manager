import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)


def calculate_average_price(products):
    total = 0
    for product in products:
        total += product["price"]
    count = len(products)
    average = total / count
    return average


average_price_result = calculate_average_price(products)


def calculate_total_inventory_value(products):
    total = 0
    for product in products:
        total += product["price"] * product["stock"]
    return total


inventory_value_result = calculate_total_inventory_value(products)
