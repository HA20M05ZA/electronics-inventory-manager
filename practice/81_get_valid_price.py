import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)


def get_valid_price():
    try:
        price = float(input("Enter price: "))
        return price
    except ValueError:
        print("Please enter valid number.")
        return None


result = get_valid_price()
print(result)
