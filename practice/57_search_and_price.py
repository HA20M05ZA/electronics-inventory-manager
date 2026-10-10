import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)


def search_and_filter_by_price(products, search, minimum_price, maximum_price):
    select = []
    for product in products:
        if (
            (
                search in product["name"].lower()
                or search in product["brand"].lower()
                or search in product["category"].lower()
            )
            and product["price"] <= maximum_price
            and product["price"] >= minimum_price
        ):
            select.append(product)
    return select


search = input("What are you looking for? ").lower().strip()
minimum_price = float(input("Minimum price: "))
maximum_price = float(input("Maximum price: "))

result = search_and_filter_by_price(products, search, minimum_price, maximum_price)

print("Products by Search and Price ")
print("-" * 20)
for product in result:
    print(f"{product['name']} - ${product['price']}")
