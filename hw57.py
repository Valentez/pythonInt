"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки,
также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
"""

import json

export_list = []
dict_plus = {}
dict_minus = {}
with open("hw57.txt") as file:
    profit_list = []
    for l in file.readlines():
        name, _, revenue, costs = l.rstrip().split()
        profit = int(revenue) - int(costs)
        if profit > 0:
            profit_list.append(profit)
            dict_plus.update({name: profit})
        else:
            dict_minus.update({name: profit})
    export_list.append(dictPlus)
    export_list.append(dictMinus)
    export_list.append({"avarage_profit": sum(profit_list)/len(profit_list)})

with open("hw57.json", "w") as file:
    json.dump(export_list, file)
