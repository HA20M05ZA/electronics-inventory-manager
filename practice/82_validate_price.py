import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)


def get_valid_price():
    try:
        price = float(input("Enter price: "))
        if price < 0:
            print("Invalid price!")
            return None
        else:
            print("Valid price")
            return price
    except ValueError:
        print("Invalid price")
        return None


result = get_valid_price()
print(result)
