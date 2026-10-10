import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)

total = 0
for product in products:
    total += product["price"]

number_of_products = len(products)
average = total / number_of_products

above_average = 0
for product in products:
    if product["price"] > average:
        above_average += 1

print(f"Product above average: {above_average}")
