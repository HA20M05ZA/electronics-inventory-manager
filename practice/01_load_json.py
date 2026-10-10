import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)

for product in products:
    print(product["name"])
