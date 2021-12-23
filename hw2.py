"""
2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются
элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний
сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

inlist = input("Input elements for list with space: ")
inlist = inlist.split()
for i in range(0, len(inlist)-1, 2):
    inlist[i], inlist[i+1] = inlist[i+1], inlist[i]
print(inlist)
