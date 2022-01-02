"""
Реализовать функцию my_func(),
которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
"""


def func(a, b, c):
    mylist = [a, b, c]
    mylist.sort(reverse=True)
    return sum(mylist[:2])


print(func(100.6, 10, -1000))
