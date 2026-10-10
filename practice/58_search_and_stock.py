import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)


def search_and_filter_by_stock(products, search, minimum_stock):
    select = []
    for product in products:
        if (
            search in product["name"].lower()
            or search in product["brand"].lower()
            or search in product["category"].lower()
        ) and product["stock"] >= minimum_stock:
            select.append(product)
    return select


search = input("What are you looking for? ").lower().strip()
minimum_stock = int(input("Minimum stock: "))


result = search_and_filter_by_stock(products, search, minimum_stock)

print("Products by Search and Price ")
print("-" * 20)
for product in result:
    print(f"{product['name']} - {product['stock']} in stock")
