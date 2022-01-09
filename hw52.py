"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
with open("hw52.txt") as file:
    fileLines = file.readlines()
    print("Value of strings in file: ", len(fileLines))
    for lineNumber, l in enumerate(fileLines, 1):
        print(f"Value of words in string {lineNumber}:", len(l.split()))
