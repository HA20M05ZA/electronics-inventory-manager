import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)


def filter_by_stock_status(products, status):
    in_stock = []
    out_stock = []
    for product in products:
        if status == "in stock" and product["stock"] > 0:
            in_stock.append(product)
        elif status == "out of stock" and product["stock"] == 0:
            out_stock.append(product)
    if status == "in stock":
        return in_stock
    elif status == "out of stock":
        return out_stock


status = input("Enter status: ").lower().strip()
result = filter_by_stock_status(products, status)
for product in result:
    print(f"{product['name']} - ${product['price']} - {product['stock']} in stock")
