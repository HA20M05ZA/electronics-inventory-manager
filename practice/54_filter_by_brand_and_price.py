import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)
brand = input("Enter brand: ").lower().strip()
minimum_price = float(input("Enter minimum price: "))
maximum_price = float(input("Enter maximum price: "))


def filter_by_brand_and_price(products, brand, minimum_price, maximum_price):
    select = []
    for product in products:
        if (
            product["brand"].lower() == brand
            and product["price"] <= maximum_price
            and product["price"] >= minimum_price
        ):
            select.append(product)
    return select


result = filter_by_brand_and_price(products, brand, minimum_price, maximum_price)
print("Products by Brand and Price Range")
print("-" * 20)
for product in result:
    print(f"{product['name']} - ${product['price']}")
