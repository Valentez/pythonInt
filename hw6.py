"""
6.  Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
    но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
    Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
    Каждое слово состоит из латинских букв в нижнем регистре.
    Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
    Необходимо использовать написанную ранее функцию int_func().
"""


int_func = lambda word: word.title()

input_string = input("Введите строку: ")
result_string_list = []
input_words = input_string.split()
for element in input_words:
    result_string_list.append(int_func(element))

print(" ".join(result_string_list))
