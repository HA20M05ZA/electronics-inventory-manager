import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)


def filter_by_brand_and_stock_status(products, brand, status):
    in_stock = []
    out_stock = []
    for product in products:
        if product["brand"].lower() == brand and product["stock"] > 0:
            in_stock.append(product)
        elif product["brand"].lower() == brand and product["stock"] == 0:
            out_stock.append(product)
    if status == "in stock":
        return in_stock
    elif status == "out of stock":
        return out_stock


brand = input("Enter brand: ").lower().strip()
status = input("Enter status: ").lower().strip()
result = filter_by_brand_and_stock_status(products, brand, status)

print("Brand and Stock status")
print("=" * 20)
for product in result:
    print(f"{product['name']} - ${product['price']} stock {product['stock']}")
