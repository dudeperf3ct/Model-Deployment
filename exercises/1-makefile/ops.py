def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError as e_info:
        raise ZeroDivisionError from e_info