"""
1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""


mylist = [3.14, 'kote', (5, 7, 11), {'hw1': 1, 'hw2':0}, [100, 200, 300], set([500, 600, 700])]
for i in mylist:
    print(type(i))
