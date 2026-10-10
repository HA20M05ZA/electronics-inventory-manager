import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)

product_in_stock = 0
product_not_in_stock = 0
total_products = len(products)

for product in products:
    if product["stock"] != 0:
        product_in_stock += 1
    elif product["stock"] == 0:
        product_not_in_stock += 1

total_inventory_value = 0
for product in products:
    total = product["price"] * product["stock"]
    total_inventory_value += total

print("==" * 13)
print("   INVENTORY STATISTICS   ")
print("==" * 13)

print(
    f"Total products: {total_products}\nProducts in stock: {product_in_stock}\nOut of stock: {product_not_in_stock}\nTotal inventory value: ${total_inventory_value}"
)
