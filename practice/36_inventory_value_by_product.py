import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)

total_inventory_value = 0
for product in products:
    inventory_value = product["price"] * product["stock"]
    print(f"{product['name']} - ${inventory_value}")
    total_inventory_value += inventory_value

print("-" * 20)
print(f"Total inventory value: ${total_inventory_value}")
