import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)


def get_valid_stock():
    try:
        stock = int(input("Enter stock: "))
        if stock < 0:
            print("Invalid stock!")
            return None
        else:
            print("Valid stock")
            return stock
    except ValueError:
        print("Invalid stock")
        return None


result = get_valid_stock()
print(result)
