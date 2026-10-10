def is_positive(number):
    return number > 0


def run_function(function, value):
    value_of = function(value)
    print(value_of)


run_function(is_positive, 7)
run_function(is_positive, -3)
