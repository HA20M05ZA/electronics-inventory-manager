import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)


def filter_by_category(products, category):
    select = []
    for product in products:
        if product["category"].lower() == category:
            select.append(product)
    return select


category = input("Enter category: ").lower().strip()
result = filter_by_category(products, category)

print(f"{category.capitalize()} Products")
print("-" * 20)
for product in result:
    print(f"{product['name']} - ${product['price']}")
