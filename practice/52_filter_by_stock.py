import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)

minimum_stock = int(input("Enter minimum stock: "))


def filter_by_stock(products, minimum_stock):
    select = []
    for product in products:
        if product["stock"] >= minimum_stock:
            select.append(product)
    return select


result = filter_by_stock(products, minimum_stock)
print("Minimum stock Products")
print("-" * 20)
for product in result:
    print(f"{product['name']} - {product['stock']} in stock")
