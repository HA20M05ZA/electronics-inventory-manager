import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)

minimum_price = float(input("Enter minimum price: "))
maximum_price = float(input("Enter maximum price: "))


def filter_by_price_range(products, minimum_price, maximum_price):
    select = []
    for product in products:
        if product["price"] >= minimum_price and product["price"] <= maximum_price:
            select.append(product)
    return select


result = filter_by_price_range(products, minimum_price, maximum_price)
print("Products in Price Range")
print("-" * 20)
for product in result:
    print(f"{product['name']} - ${product['price']}")
