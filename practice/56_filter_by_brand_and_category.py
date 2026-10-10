import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)


def filter_by_brand_and_category(products, brand, category):
    select = []
    for product in products:
        if (
            product["brand"].lower() == brand
            and product["category"].lower() == category
        ):
            select.append(product)

    return select


brand = input("Enter brand: ").lower().strip()
category = input("Enter category: ").lower().strip()

result = filter_by_brand_and_category(products, brand, category)
print("Products by Brand and Category")
print("-" * 20)
for product in result:
    print(f"{product['name']} - ${product['price']}")
