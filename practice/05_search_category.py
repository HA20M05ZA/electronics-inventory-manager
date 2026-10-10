import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)

found = False
search = input("Enter category: ").lower()
print(f"Products in {search} category")
print("-" * 20)


for product in products:
    if search == product["category"].lower():
        print(f"{product['name']} - {product['brand']} - ${product['price']}")
        found = True
if not found:
    print("No products found for this category.")
