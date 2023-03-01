"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
with open("hw52.txt") as file:
    file_lines = file.readlines()
    print("Value of strings in file: ", len(file_lines))
    for line_number, l in enumerate(file_lines, 1):
        print(f"Value of words in string {line_number}:", len(l.split()))
