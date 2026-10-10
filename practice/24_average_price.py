import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)

total_price = 0
for product in products:
    total_price += product["price"]

number_of_products = len(products)
average = total_price / number_of_products

print("Average product price")
print("-" * 20)
print(f"${average:.2f}")
