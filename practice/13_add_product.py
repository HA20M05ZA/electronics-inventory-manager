import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)

product_name = input("Enter product name: ").capitalize()
product_brand = input("Enter product brand: ").capitalize()
product_category = input("Enter product category: ").lower()
product_price = float(input("Enter product price: "))
product_stock = int(input("Enter product stock: "))

new_product = {
    "name": product_name,
    "brand": product_brand,
    "category": product_category,
    "price": product_price,
    "stock": product_stock,
}

products.append(new_product)
with open("../data/electronics.json", "w") as file:
    json.dump(products, file, indent=4)
