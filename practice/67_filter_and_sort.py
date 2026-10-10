import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)


def filter_and_sort(products, category, minimum_price, maximum_price, sort_by):
    select = []
    for product in products:
        if (
            product["category"].lower() == category
            and minimum_price <= product["price"] <= maximum_price
        ):
            select.append(product)

    if sort_by == "price":
        sort_by_price = sorted(select, key=lambda product: product["price"])
        return sort_by_price
    elif sort_by == "stock":
        sort_by_stock = sorted(select, key=lambda product: product["stock"])
        return sort_by_stock


category = input("Category: ").lower().strip()
minimum_price = float(input("Minimum price: "))
maximum_price = float(input("Maximum price: "))
sort_by = input("Sort by: ").lower()
result = filter_and_sort(products, category, minimum_price, maximum_price, sort_by)
for product in result:
    print(f"{product['name']} - ${product['price']} - {product['stock']} in stock")
