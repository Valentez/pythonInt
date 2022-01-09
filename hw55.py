"""
 Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open("hw55.txt", "w") as fileWrite:
    inputNum = input("please, input numbers via space: ")
    print(inputNum, file=fileWrite)

with open("hw55.txt") as fileRead:
    content = fileRead.read().rstrip().split()
    listNum = [int(num) for num in content if num.isdigit()]
    print(listNum)
    print(sum(listNum))
