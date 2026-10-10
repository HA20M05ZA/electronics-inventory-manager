import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)


def filter_sort_inventory_value(products, category, minimum_price, sort_by):
    select = []
    total = 0

    for product in products:
        if product["category"] == category and minimum_price <= product["price"]:
            select.append(product)
            total += product["price"] * product["stock"]
    if sort_by == "price":
        sort_by_price = sorted(select, key=lambda product: product["price"])
        return sort_by_price, total
    elif sort_by == "stock":
        sort_by_stock = sorted(select, key=lambda product: product["stock"])
        return sort_by_stock, total


category = input("Category: ").lower().strip()
minimum_price = float(input("Minimum price: "))
sort_by = input("Sort by: ").lower().strip()

result, total = filter_sort_inventory_value(products, category, minimum_price, sort_by)
for product in result:
    print(f"{product['name']} - ${product['price']} - {product['stock']} in stock")
print(f"\nTotal Inventory Value: {total:.2f}")
