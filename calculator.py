def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y
def power(x, y):
    return x ** y

def sqrt(x):
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number!")
    return x ** 0.5