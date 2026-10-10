import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)

print("--" * 20)

found = False
search = input("Enter product name: ").lower()

for product in products:
    if search in product["name"].lower():
        print(
            f"Product found!\n"
            f"Name: {product['name']}\n"
            f"Brand: {product['brand']}\n"
            f"Price: ${product['price']}\n"
            f"Stock: {product['stock']}"
        )

        found = True
        break

if not found:
    print("Product not found.")
