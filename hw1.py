"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "You cannot divide by zero"


a, b = map(float, input("Please, input two numbers: ").split())
print(division(a, b))
