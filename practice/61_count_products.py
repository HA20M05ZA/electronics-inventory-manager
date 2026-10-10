import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)


def count_products(products):
    count = 0
    for product in products:
        count += 1
    return count


result = count_products(products)
print(result)
