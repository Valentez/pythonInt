"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
sumary = 0
with open("hw53.txt") as file:
    lines = file.readlines()
    for l in lines:
        surname, salary = l.split()
        sumary += int(salary)
        if int(salary) < 20000:
            print("Have salary less then 20k: ", surname)
print("Middle salary: ", sumary/len(l))
