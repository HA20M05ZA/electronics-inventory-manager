import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)

brand = input("Enter brand: ").lower().strip()


def filter_by_brand(products, brand):
    select = []
    for product in products:
        if product["brand"].lower() == brand:
            select.append(product)
    return select


result = filter_by_brand(products, brand)

print(f"{brand.capitalize()} Products")
print("=" * 20)
for product in result:
    print(f"{product['name']} - ${product['price']}")
