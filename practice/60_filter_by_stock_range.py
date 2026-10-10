import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)


def filter_by_stock_range(products, minimum_stock, maximum_stock):
    select = []
    for product in products:
        if minimum_stock <= product["stock"] <= maximum_stock:
            select.append(product)
    return select


minimum = int(input("Minimum stock: "))
maximum = int(input("Maximum stock: "))

result = filter_by_stock_range(products, minimum_stock=minimum, maximum_stock=maximum)
print("Product in stock")
print("-" * 20)
for product in result:
    print(f"{product['name']} - ${product['price']} - in stock {product['stock']}")
