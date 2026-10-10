import json

with open("../data/electronics.json", "r") as file:
    products = json.load(file)


def get_valid_name():
    name = input("Enter new name: ").strip().capitalize()
    if name == "":
        return None
    else:
        return name


def get_valid_brand():
    brand = input("Enter new brand: ").strip().capitalize()
    if brand == "":
        return None
    else:
        return brand


def get_valid_category():
    category = input("Enter new category: ").strip().capitalize()
    if category == "":
        return None
    else:
        return category


def get_valid_price():
    try:
        price = float(input("Enter price: "))

        if price < 0:
            print("Invalid price!")
            return None

        return price

    except ValueError:
        print("Invalid price!")
        return None


def get_valid_stock():
    try:
        stock = int(input("Enter stock: "))

        if stock < 0:
            print("Invalid stock!")
            return None

        return stock

    except ValueError:
        print("Invalid stock!")
        return None


def get_valid_product_data():

    name = get_valid_name()
    brand = get_valid_brand()
    category = get_valid_category()

    price = get_valid_price()
    stock = get_valid_stock()

    if (
        price is None
        or stock is None
        or name is None
        or brand is None
        or category is None
    ):
        return None

    product = {
        "name": name,
        "brand": brand,
        "category": category,
        "price": price,
        "stock": stock,
    }

    return product


def add_product(products, product):
    products.append(product)


def save_products(products):
    with open("../data/electronics.json", "w") as file:
        json.dump(products, file, indent=4)


def product_name_exists(products, name):
    for product in products:
        if product["name"].lower() == name.lower():
            return True

    return False


def confirm_action():
    while True:
        confirm = input("Are you sure? (yes/no): ").strip().lower()
        if confirm == "yes":
            return True
        elif confirm == "no":
            return False
        else:
            print("Please enter yes or no.\n")


def create_and_add_product(products):
    product = get_valid_product_data()

    if product is None:
        print("Nothing added!")
    else:
        exists = product_name_exists(products, product["name"].lower())
        if exists:
            print("Product already exists ❌")
        else:
            confirm = confirm_action()
            if confirm:
                add_product(products, product)
                save_products(products)
                print("Product is added ✅")
            else:
                print("Addition cancelled ❌")
                return


def find_product(products, search):
    for product in products:
        if search.lower().strip() == product["name"].lower():
            return product
    return None


def update_product_price(products, search, new_price):
    product = find_product(products, search)
    if product is None:
        print("Product not found ❌")
        return False

    product["price"] = new_price
    save_products(products)
    return True


def update_product_name(products, search, new_name):
    product = find_product(products, search)

    if product is None:
        print("Product not found ❌")
        return False

    for item in products:
        if item is product:
            continue

        if new_name.strip().lower() == item["name"].strip().lower():
            print("Product already exists ❌")
            return False

    product["name"] = new_name
    save_products(products)
    return True


def update_product_brand(products, search, new_brand):
    product = find_product(products, search)
    if product is None:
        print("Product not found ❌")
        return False
    product["brand"] = new_brand
    save_products(products)
    return True


def update_product_category(products, search, new_category):
    product = find_product(products, search)
    if product is None:
        print("Product not found ❌")
        return False
    product["category"] = new_category
    save_products(products)
    return True


def update_product_stock(products, search, new_stock):
    product = find_product(products, search)
    if product is None:
        print("Product not found!")
        return False
    product["stock"] = new_stock
    save_products(products)
    return True


def get_product_search():
    search = input("Search: ").strip().lower()
    return search


def show_update_result(result):
    if result:
        print("Update successful✅")
    else:
        print("Update failed ❌")


def handle_invalid_input(value):
    if value is None:
        print("Invalid input!")
        return False
    else:
        return True


def get_update_choice():
    while True:
        try:
            select = int(
                input("""
1. Update price
2. Update stock
3. Update name
4. Update brand
5. Update category
            
                """)
            )
            if 0 < select <= 5:
                return select
            else:
                print("Invalid choice!")
        except ValueError:
            print("Invalid choice!")


def perform_product_update(products, search, select):
    if select == 1:
        new_price = get_valid_price()
        helper = handle_invalid_input(new_price)
        if helper:
            result = update_product_price(products, search, new_price)
            show_update_result(result)

    elif select == 2:
        new_stock = get_valid_stock()
        helper = handle_invalid_input(new_stock)
        if helper:
            result = update_product_stock(products, search, new_stock)
            show_update_result(result)

    elif select == 3:
        new_name = get_valid_name()
        helper = handle_invalid_input(new_name)
        if helper:
            result = update_product_name(products, search, new_name)
            show_update_result(result)

    elif select == 4:
        new_brand = get_valid_brand()
        helper = handle_invalid_input(new_brand)
        if helper:
            result = update_product_brand(products, search, new_brand)
            show_update_result(result)

    elif select == 5:
        new_category = get_valid_category()
        helper = handle_invalid_input(new_category)
        if helper:
            result = update_product_category(products, search, new_category)
            show_update_result(result)


def get_product_or_none(products, search):
    product = find_product(products, search)
    if product is None:
        print("Product not found ❌")
        return
    return product


def update_product(products, search):
    product = get_product_or_none(products, search)
    if product is None:
        return
    confirm = confirm_action()
    if confirm:
        select = get_update_choice()
        perform_product_update(products, search, select)

    else:
        print("Update cancelled.")


def delete_product_from_menu(products, search):
    product = get_product_or_none(products, search)
    if product is None:
        return

    confirm = confirm_action()
    if confirm:
        products.remove(product)
        save_products(products)
        print("Product removed ✅")
    else:
        print("Deletion cancelled.")


def show_menu():
    print("""
1. Add product
2. Delete product
3. Update product
4. Stop
""")


def delete_product_menu(products):
    search = get_product_search()
    delete_product_from_menu(products, search)


def update_product_menu(products):
    search = get_product_search()
    update_product(products, search)


def get_valid_choice():
    while True:
        try:
            show_menu()
            select = int(input("Select number: "))
            if select <= 4 and select > 0:
                return select
            else:
                print("Invalid choice!")
        except ValueError:
            print("Invalid choice!")


def add_product_menu(products):
    create_and_add_product(products)


def stop_program():
    print("Program closed successfully.")


def main_menu(products):
    while True:
        select = get_valid_choice()

        if select == 1:
            add_product_menu(products)

        elif select == 2:
            delete_product_menu(products)

        elif select == 3:
            update_product_menu(products)

        elif select == 4:
            stop_program()
            return


main_menu(products)
