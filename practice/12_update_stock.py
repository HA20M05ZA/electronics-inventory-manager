import json
import sys

with open("../data/electronics.json", "r") as file:
    products = json.load(file)

product_name = input("Enter product name: ").lower()
new_stock = int(input("Enter new stock: "))

found = False
for product in products:
    if product_name == product["name"].lower():
        product["stock"] = new_stock
        print("Stock updated successfully!")
        print(f"{product['name']} - New stock: {product['stock']}")
        found = True

if not found:
    print("Product not found. ")
    sys.exit()


with open("../data/electronics.json", "w") as file:
    json.dump(products, file, indent=4)
