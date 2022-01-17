"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Stuff(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def get_cons(self):
        pass


class Coat(Stuff):
    def __init__(self, param):
        super().__init__(param)
        print(f'New coat with size {self.param}')

    @property
    def get_cons(self):
        return round(self.param / 6.5 + 0.5, 2)


class SuitUP(Stuff):
    def __init__(self, param):
        super().__init__(param)
        print(f'Barney says - Suit UP! {self.param}')

    @property
    def get_cons(self):
        return round(self.param * 2 + 0.3, 2)


coat = Coat(42)
print(f'Consumption for my coat is: {coat.get_cons}')
suit = SuitUP(1.78)
print(f'Consumption for my suit is: {suit.get_cons}')
print(f'Total is: {coat.get_cons + suit.get_cons}')
