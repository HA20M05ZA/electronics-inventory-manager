import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)

lowest_price = float("inf")
cheapest_product = None

for product in products:
    if product["price"] < lowest_price:
        lowest_price = product["price"]
        cheapest_product = product["name"]

print(f"The cheapest product is {cheapest_product}\nPrice: ${lowest_price}")
