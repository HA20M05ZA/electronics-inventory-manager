import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)


def multi_criteria_search(
    products,
    search,
    brand,
    category,
    minimum_price,
    maximum_price,
    minimum_stock,
    maximum_stock,
):
    select = []
    for product in products:
        if (
            (
                search in product["name"].lower()
                or search in product["brand"].lower()
                or search in product["category"].lower()
                or search == ""
            )
            and (product["brand"].lower() == brand or brand == "")
            and (product["category"].lower() == category or category == "")
            and minimum_price <= product["price"] <= maximum_price
            and minimum_stock <= product["stock"] <= maximum_stock
        ):
            select.append(product)

    return select


search = input("Search: ").lower().strip()
brand = input("Brand: ").lower().strip()
category = input("Category: ").lower().strip()
minimum_price = float(input("Minimum price: "))
maximum_price = float(input("Maximum price: "))
minimum_stock = int(input("Minimum stock: "))
maximum_stock = int(input("Maximum stock: "))

result = multi_criteria_search(
    products,
    search,
    brand,
    category,
    minimum_price,
    maximum_price,
    minimum_stock,
    maximum_stock,
)

print("Advance search")
print("-" * 20)
for product in result:
    print(f"{product['name']} - ${product['price']} - {product['stock']} in stock")
