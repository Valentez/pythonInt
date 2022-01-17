"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем
нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
завершиться с ошибкой.
"""


class ErrorDivision(Exception):
    def __init__(self):
        self.txt = 'My division by joy'


def division(divident, divisor):
    try:
        if divisor == 0:
            raise ErrorDivision
        print(divident / divisor)
    except ErrorDivision as error:
        print(error.txt)


a, b = map(float, input("Please, input two numbers: ").split())
division(a, b)
