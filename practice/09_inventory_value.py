import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)

total_value = 0
for product in products:
    total_value += product["price"] * product["stock"]

print(f"Total inventory value: ${total_value}")
