import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)


def count_products_by_brand(products, brand):
    select = 0
    for product in products:
        if product["brand"].lower() == brand:
            select += 1
    return select


brand = input("Enter brand: ").lower().strip()
result = count_products_by_brand(products, brand)
print(result)
