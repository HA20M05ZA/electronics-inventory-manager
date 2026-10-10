import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)


def filter_sort_limit(products, category, minimum_price, sort_by, limit):
    select = []
    for product in products:
        if product["category"] == category and minimum_price <= product["price"]:
            select.append(product)
    if sort_by == "price":
        sort_by_price = sorted(select, key=lambda product: product["price"])[:limit]
        return sort_by_price
    elif sort_by == "stock":
        sort_by_stock = sorted(select, key=lambda product: product["stock"])[:limit]
        return sort_by_stock


category = input("Category: ").lower().strip()
minimum_price = float(input("Minimum price: "))
sort_by = input("Sort by: ").lower().strip()
limit = int(input("Limit: "))
result = filter_sort_limit(products, category, minimum_price, sort_by, limit)
for product in result:
    print(f"{product['name']} - ${product['price']} - {product['stock']} in stock ")
