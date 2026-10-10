def calculate_inventory_value(price, stock):
    total = price * stock
    return total


def calculate_average_price(total_price, count):
    return total_price / count


print(calculate_average_price(1700, 2))
