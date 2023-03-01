"""
5.	  Реализовать класс Stationery (канцелярская принадлежность).
      Определить в нем атрибут title (название) и метод draw (отрисовка).
      Метод выводит сообщение “Запуск отрисовки.”
      Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
      В каждом из классов реализовать переопределение метода draw.
      Для каждого из классов методы должен выводить уникальное сообщение.
      Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationary:
    def __init__(self, title):
        self.__title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationary):
    # def __init__(self, title):
    #     super().__init__(title)

    def draw(self):
        print(f'We are drawing by {self.title}')


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'We are drawing by {self.title}')


class Handle(Stationary):

    def draw(self):
        print(f'We are drawing by {self.title}')


pen = Pen("pen")
pencil = Pencil("pencil")
handle = Handle("handle")
pen.draw()
pencil.draw()
handle.draw()
# stat = Stationary("title")
# print(stat.title)
