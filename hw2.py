"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def profile(**kwargs):
    return f"Name: {kwargs['name']}, Surname: {kwargs['surname']}, " \
           f"Year of birth: {kwargs['yob']}, City: {kwargs['city']}, " \
           f"E-Mail: {kwargs['mail']}, Phone: {kwargs['phone']}"


print(profile(name='Alex', surname='Dunin', yob='91', city='Msc', mail='kote@manul.com', phone='13666'))
