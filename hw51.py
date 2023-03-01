"""
1. Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""

input_str = input("Please, input yours string: ")
with open("hw51.txt", "a") as file:
    while input_str:
        file.write(f"{input_str}\n")
        input_str = input("Please, input yours string(for exit, input 'q'): ")
        if input_str == "q":
            file.close()
            break
file = open("hw51.txt", "r")
print(file.read())
file.close()
