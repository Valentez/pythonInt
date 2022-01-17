"""
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Run draw')


class Pen(Stationary):

    def draw(self):
        super().draw()
        print(f"We are drawing by {self.title}")


class Pencil(Stationary):

    def draw(self):
        super().draw()
        print(f"We are drawing by {self.title}")


class Handle(Stationary):

    def draw(self):
        super().draw()
        print(f"We are drawing by {self.title}")


pen = Pen('pen')
pencil = Pencil('pencil')
handle = Handle('handle')
pen.draw()
pencil.draw()
handle.draw()
