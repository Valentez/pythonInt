"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

try:
    number_of_month = int(input("Введите номер месяца числом от 1 до 12: "))
except ValueError:
    print("Неверно введен номер месяца")
else:
    winter = [12, 1, 2]
    spring = [3, 4, 5]
    summer = [6, 7, 8]
    autumn = [9, 10, 11]

    if number_of_month in winter:
        print('Зима')
    elif number_of_month in spring:
        print('Весна')
    elif number_of_month in summer:
        print('Лето')
    elif number_of_month in autumn:
        print('Осень')
    else:
        print('Время года не определено')

    seasons_dict = {}
    seasons_dict = seasons_dict.fromkeys([12, 1, 2], 'Зима')
    seasons_dict.update({}.fromkeys([3, 4, 5], 'Весна'))
    seasons_dict.update({}.fromkeys([6, 7, 8], 'Лето'))
    seasons_dict.update({}.fromkeys([9, 10, 11], 'Осень'))

    # print(seasons_dict)

    for season_month_number, season in seasons_dict.items():
        if number_of_month == season_month_number:
            print(season)
            break
    else:
        print('Время года не определено')

    print(seasons_dict[number_of_month])
