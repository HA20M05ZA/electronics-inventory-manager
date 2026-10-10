import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)


def filter_by_category_and_price(products, category, minimum_price, maximum_price):
    select = []
    for product in products:
        if (
            product["category"].lower() == category
            and product["price"] <= maximum_price
            and product["price"] >= minimum_price
        ):
            select.append(product)

    return select


category = input("Enter category: ").lower().strip()
minimum_price = float(input("minimum price: "))
maximum_price = float(input("maximum price: "))
result = filter_by_category_and_price(products, category, minimum_price, maximum_price)

print("Products by Category and Price Range")
print("-" * 20)
for product in result:
    print(f"{product['name']} - ${product['price']}")
