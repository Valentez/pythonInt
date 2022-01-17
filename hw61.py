"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод
running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать переключение
светофора в режимы: красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить
соответствующее сообщение и завершать скрипт.
"""
from itertools import cycle
from time import sleep


class TrafficLight:
    colorQueue = ("R", "Y", "G")
    timeQueue = (7, 2, 5)
    message = ("Red - stop!", "Yellow - attention!", "Green - GO!GO!GO!")

    def __init__(self, color):
        self.__color = color

    def running(self):
        myCycle = cycle(self.colorQueue)
        for trafficColor in myCycle:
            if self.__color == trafficColor:
                print(self.message(self.colorQueue.index(self.__color)))
                sleep(self.timeQueue(self.colorQueue.index(self.__color)))
                self.__color = next(myCycle)


myTraffic = TrafficLight("Y")
myTraffic.running()
