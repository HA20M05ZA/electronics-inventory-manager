import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)


def advanced_search(products, search, minimum_price, maximum_price, minimum_stock):
    select = []
    for product in products:
        if (
            (
                search in product["name"].lower()
                or search in product["brand"].lower()
                or search in product["category"].lower()
            )
            and minimum_price <= product["price"] <= maximum_price
            and product["stock"] >= minimum_stock
        ):
            select.append(product)
    return select


search = input("What are you looking for? ").lower().strip()
minimum_price = float(input("minimum price: "))
maximum_price = float(input("maximum price: "))
minimum_stock = int(input("Minimum stock: "))

result = advanced_search(products, search, minimum_price, maximum_price, minimum_stock)

print("Products by Search🔍 Stock📦 and Price💵 ")
print("-" * 20)
for product in result:
    print(f"{product['name']} - ${product['price']} - {product['stock']} in stock")
