import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)

in_stock = 0
out_stock = 0

for product in products:
    if product["stock"] > 0:
        in_stock += 1
    else:
        out_stock += 1

count = 0
inventory_value = 0
total_price = 0
for product in products:
    inventory_value += product["price"] * product["stock"]
    total_price += product["price"]
    count = len(products)
average_price = total_price / count

print("Inventory Report🖨️")
print(f"Total products: {count}")
print(f"Products in stock: {in_stock}")
print(f"Out of stock: {out_stock}")
print(f"Average price: ${average_price:.2f}")
print(f"Total inventory value: ${inventory_value}")
