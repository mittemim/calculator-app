def add(x, y):

    '''Вычисление суммы двух чисел'''

    return x + y

def subtract(x, y):

    '''Вычисление разности двух чисел'''

    return x - y

def multiply(x, y):

    '''Вычисление произведения двух чисел'''

    return x * y

def divide(x, y):

    '''Вычисление частного двух чисел'''

    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y
def power(x, y):

    '''Вычисление результата возведения заданного числа в заданную степень'''

    return x ** y

def sqrt(x):

    '''Вычисление результата извлечения квадратного корня из заданного числа'''

    if x < 0:
        raise ValueError("Cannot compute square root of a negative number!")
    return x ** 0.5