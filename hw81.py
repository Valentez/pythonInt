"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например,
месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""

class Date:
    def __init__(self, date):
        self.date = date

    def extract_data(self):
        try:
            day, month, year = self.date.split('/')
            return int(day), int(month), int(year)
        except Exception as e:
            print(f'Cant mark date from string {e}')

    @staticmethod
    def validate_data(date_input):
        try:
            day, month, year = date_input
            if day not in range(1, 32):
                raise ValueError('Wrong day')
            elif month not in range(1, 13):
                raise ValueError('Wrong month')
            elif year not in range(-6000, 2022):
                raise ValueError('Wrong year. Gosh bless you')
        except ValueError as e:
            print(e)
        else:
            print("Success!")


my_date_cls = Date('13/07/-6000000')
my_date = my_date_cls.extract_data()
print(my_date)
if my_date:
    my_date_cls.validate_data(my_date)
