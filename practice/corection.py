import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)

ask_for_correcting = input("what you need to correct: ")
correcting = input("What is the correction: ")

for product in products:
    if product["name"] == ask_for_correcting:
        product["name"] = correcting

with open("../data/electronics.json", "w") as file:
    json.dump(products, file, indent=4)
