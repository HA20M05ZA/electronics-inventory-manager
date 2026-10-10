import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)


def find_first_product(products, search):
    found = None
    for product in products:
        if (
            search in product["name"].lower()
            or search in product["brand"].lower()
            or search in product["category"].lower()
        ):
            found = product

            break
    return found


search = input("Search: ").lower().strip()
result = find_first_product(products, search)
if result is None:
    print("Product not found!")
else:
    print(f"{result['name']} - ${result['price']}")
