import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)


def filter_sort_report(products, category, minimum_price, sort_by):
    select = []
    count = 0
    total = 0
    price = []
    for product in products:
        if product["category"] == category and minimum_price <= product["price"]:
            select.append(product)
            price.append(product["price"])
            count += 1
            total += product["price"] * product["stock"]

    if sort_by not in ["price", "stock"]:
        print("Invalid sort option.")
        return None

    if not price:
        print("No products found.")
        return None

    if sort_by == "stock":
        sort_by_stock = sorted(select, key=lambda product: product["stock"])

        average = sum(price) / len(price)

        return sort_by_stock, count, average, total

    elif sort_by == "price":
        sort_by_price = sorted(select, key=lambda product: product["price"])

        average = sum(price) / len(price)

        return sort_by_price, count, average, total


category = input("Category: ").lower().strip()
minimum_price = float(input("Minimum price: "))
sort_by = input("Sort by: ").lower().strip()

result = filter_sort_report(products, category, minimum_price, sort_by)


if result is None:
    print("No report generated.")

else:
    result, count, average, total = result

    for product in result:
        print(f"{product['name']} - ${product['price']} - {product['stock']} in stock")

    print(f"\nCount: {count}")
    print(f"Average price: ${average:.2f}")
    print(f"Total inventory value: ${total:.2f}")
