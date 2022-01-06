"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3,
а при достижении числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие,
при котором повторение элементов списка будет прекращено.
"""
from itertools import count, cycle

interCount = 0
countList = []


def generate(start):
    for i in count(start):
        if i > start+10:
            break
        yield i


for i in generate(3):
    countList.append(i)
print(countList)

for i in cycle(countList):
    if i == countList[0]:
        interCount += 1
    if interCount < 3:
        print(i)
    else:
        break
