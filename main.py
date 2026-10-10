import json

with open("data/electronics.json", "r") as file:
    products = json.load(file)


def show_products(products):
    if not products:
        print("No products found.")
    else:
        for product in products:
            print(
                f"""
Name: {product["name"]}
Brand: {product["brand"]}
Category: {product["category"]}
Price: {product["price"]}
Stock: {product["stock"]}
----------------------
"""
            )


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
    with open("data/electronics.json", "w") as file:
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
=============================
   ELECTRONICS INVENTORY
=============================

1. Show products
2. Search products
3. Add product
4. Update product
5. Delete product
6. Filter products
7. Statistics
8. Inventory report
9. Exit
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
            if select <= 9 and select > 0:
                return select
            else:
                print("Invalid choice!")
        except ValueError:
            print("Invalid choice!")


def advanced_search(products, search, minimum_price, maximum_price, minimum_stock):
    select = []
    for product in products:
        if (
            (
                search in product["name"].lower()
                or search in product["brand"].lower()
                or search in product["category"].lower()
            )
            and minimum_price <= product["price"] <= maximum_price
            and product["stock"] >= minimum_stock
        ):
            select.append(product)
    return select


def search_product_menu(products):
    search = get_product_search()
    minimum_price = get_valid_price()
    maximum_price = get_valid_price()
    minimum_stock = get_valid_stock()
    if minimum_price is None or maximum_price is None or minimum_stock is None:
        return
    result = advanced_search(
        products, search, minimum_price, maximum_price, minimum_stock
    )
    if not result:
        print("No products found.")
    else:
        show_products(result)


def filter_sort_report(products, category, minimum_price, sort_by):
    select = []
    count = 0
    total = 0
    price = []
    for product in products:
        if (
            product["category"].lower() == category.lower()
            and minimum_price <= product["price"]
        ):
            select.append(product)
            price.append(product["price"])
            count += 1
            total += product["price"] * product["stock"]

    if sort_by not in ["price", "stock"]:
        print("Invalid sort option.")
        return None

    if not price:
        print("No products found.")
        return None

    if sort_by == "stock":
        sort_by_stock = sorted(select, key=lambda product: product["stock"])

        average = sum(price) / len(price)

        return sort_by_stock, count, average, total

    elif sort_by == "price":
        sort_by_price = sorted(select, key=lambda product: product["price"])

        average = sum(price) / len(price)

        return sort_by_price, count, average, total


def filter_products_menu(products):
    category = input("Category: ").lower().strip()
    minimum_price = get_valid_price()
    sort_by = input("Sort by (price/stock): ").lower().strip()
    if minimum_price is None:
        return
    if sort_by not in ["price", "stock"]:
        print("Invalid sort option.")
        return
    result = filter_sort_report(products, category, minimum_price, sort_by)
    if result is None:
        return

    result, count, average, total = result
    if not result:
        print("No products found.")
    else:
        show_products(result)
        print(f"Count: {count}")
        print(f"Average price: ${average:.2f}")
        print(f"Total inventory value: ${total:.2f}")


def show_statistics(products):
    if not products:
        print("No products available.")
        return

    total_products = len(products)
    total_stock = sum(product["stock"] for product in products)
    average_price = sum(product["price"] for product in products) / total_products
    total_value = sum(product["price"] * product["stock"] for product in products)
    all_in_stock = all(product["stock"] > 0 for product in products)

    print("\n===== INVENTORY STATISTICS =====")
    print(f"Total products: {total_products}")
    print(f"Total stock units: {total_stock}")
    print(f"Average price: ${average_price:.2f}")
    print(f"Total inventory value: ${total_value:.2f}")
    print(f"All products in stock: {all_in_stock}")


def show_inventory_report(products):
    if not products:
        print("No products available.")
        return

    sorted_products = sorted(products, key=lambda product: product["name"].lower())

    total_value = 0

    print("\n========== INVENTORY REPORT ==========")

    for product in sorted_products:
        product_value = product["price"] * product["stock"]
        total_value += product_value

        print(
            f"Name: {product['name']} | "
            f"Brand: {product['brand']} | "
            f"Category: {product['category']} | "
            f"Price: ${product['price']:.2f} | "
            f"Stock: {product['stock']} | "
            f"Value: ${product_value:.2f}"
        )

    print("-" * 40)
    print(f"Total products: {len(products)}")
    print(f"Total inventory value: ${total_value:.2f}")


def add_product_menu(products):
    create_and_add_product(products)


def stop_program():
    print("Program closed successfully.")


def main_menu(products):
    while True:
        select = get_valid_choice()
        if select == 1:
            show_products(products)

        elif select == 2:
            search_product_menu(products)

        elif select == 3:
            add_product_menu(products)

        elif select == 4:
            update_product_menu(products)

        elif select == 5:
            delete_product_menu(products)

        elif select == 6:
            filter_products_menu(products)

        elif select == 7:
            show_statistics(products)

        elif select == 8:
            show_inventory_report(products)

        elif select == 9:
            stop_program()
            return


main_menu(products)
