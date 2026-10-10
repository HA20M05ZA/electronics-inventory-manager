import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)

found = False
product_name = input("Enter product name: ").lower()
for product in products:
    if product["name"].lower() == product_name:
        products.remove(product)
        print("Product deleted successfully!")
        found = True
        break

if not found:
    print("Product not found.")

with open("../data/electronics.json", "w") as file:
    json.dump(products, file, indent=4)
