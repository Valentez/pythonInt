"""
2.  Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
    Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
    Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
    Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
    толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.

Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:
    def __init__(self, width, length):
        self._width = width
        self._length = length

    def get_weight_of_asphalt(self, weight_ratio, thikness):
        asphalt = self._length * self._width * weight_ratio * thikness
        return asphalt

    @property
    def square(self):
        return self._length * self._width

    @staticmethod
    def sum(a, b):
        return a+b


my_road = Road(20, 5000)
print(my_road.get_weight_of_asphalt(25, 0.5))
print(my_road.square)
print(my_road.sum(20, 50))
