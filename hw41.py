"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv


scriptName, productivity, ratePerHour, bonus = argv
print(f"Script name:{scriptName}\
    \nHours:{productivity}\
    \nRate per hour:{ratePerHour}\
    \nBonus:{bonus}\
    \nSalary:{int(productivity)*int(ratePerHour)+int(bonus)}")
