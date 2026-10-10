import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)


def filter_sort_average_count(products, category, minimum_price, sort_by):
    price = []
    select = []
    count = 0
    for product in products:
        if product["category"] == category and minimum_price <= product["price"]:
            select.append(product)
            price.append(product["price"])
            count += 1
    if sort_by == "price":
        sort_by_price = sorted(select, key=lambda product: product["price"])
        average = sum(price) / len(price)
        return sort_by_price, count, average
    elif sort_by == "stock":
        sort_by_stock = sorted(select, key=lambda product: product["stock"])
        average = sum(price) / len(price)
        return sort_by_stock, count, average


category = input("Category: ").lower().strip()
minimum_price = float(input("Minimum price: "))
sort_by = input("Sort by: ").lower().strip()

result, count, average = filter_sort_average_count(
    products, category, minimum_price, sort_by
)
for product in result:
    print(f"{product['name']} - ${product['price']} - {product['stock']} in stock")
print(f"\nCount: {count}")
print(f"\nAverage: {average:.2f}")
