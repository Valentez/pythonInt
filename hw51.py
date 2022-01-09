"""
1. Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""

inputString = input("Please, input yours string: ")
with open("hw51.txt", "a") as file:
    while inputString:
        file.write(f"{inputString}\n")
        inputString = input("Please, input yours string(for exit, input 'q'): ")
        if inputString == "q":
            file.close()
            break
file = open("hw51.txt", "r")
print(file.read())
file.close()
