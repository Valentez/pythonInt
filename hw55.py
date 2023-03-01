"""
 Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open("hw55.txt", "w") as file_write:
    input_num = input("please, input numbers via space: ")
    print(input_num, file=file_write)

with open("hw55.txt") as file_read:
    content = file_read.read().rstrip().split()
    list_num = [int(num) for num in content if num.isdigit()]
    print(list_num)
    print(sum(list_num))
