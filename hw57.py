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

exportList = []
dictPlus = {}
dictMinus = {}
with open("hw57.txt") as file:
    profitList = []
    for l in file.readlines():
        name, _, revenue, costs = l.rstrip().split()
        profit = int(revenue) - int(costs)
        if profit > 0:
            profitList.append(profit)
            dictPlus.update({name: profit})
        else:
            dictMinus.update({name: profit})
    exportList.append(dictPlus)
    exportList.append(dictMinus)
    exportList.append({"avarageProfit": sum(profitList)/len(profitList)})

with open("hw57.json", "w") as file:
    json.dump(exportList, file)
