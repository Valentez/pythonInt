"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""


from sys import argv


script_name, productivity, rate_per_hour, bonus = argv
print("Name of script: ", script_name)
print('Productivity, hours: ', productivity)
print('Rate per hour: ', rate_per_hour)
print('Bonus: ', bonus)
print('Salary: ', int(productivity) * int(rate_per_hour) + int(bonus))
