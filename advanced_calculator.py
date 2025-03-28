from calculator import add, subtract, multiply, divide, power

def factorial(n):

    '''Вычисление факториала числа'''

    if n == 0:
        return 1
    else:
        return n * factorial(n-1)