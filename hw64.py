"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
"""

class Cars:
    def __init__(self, speed, color, name, isPolice):
        self.speed = speed
        self.color = color
        self.name = name
        self.isPolice = isPolice

    def go(self):
        print(f'{self.color} {self.name} has a {self.speed} speed')

    def stop(self):
        print(f'{self.color} {self.name} stopped')

    def turn(self, direction):
        print(f'{self.color} {self.name} turn to {direction}')

    def showSpeed(self):
        print(f'Speed is {self.speed}')


class TownCar(Cars):

    def showSpeed(self):
        if self.speed > 60:
            print('Please, relax')
        else:
            Cars.showSpeed(self)


class SportCar(Cars):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, isPolice=False)


class WorkCars(Cars):

    def showSpeed(self):
        if self.speed > 40:
            print('Please, relax')


class PoliceCar(Cars):
    def __init__(self, speed, color, name):
        Cars.__init__(self, speed, color, name, isPolice=True)


myPoliceCar = PoliceCar(90, 'White', 'Lada Niva')
myPoliceCar.go()
myPoliceCar.turn('left')
myPoliceCar.stop()
myPoliceCar.showSpeed()
print()

workCar = WorkCars(85, 'black', 'Gazel', False)
workCar.go()
workCar.turn('right')
workCar.stop()
workCar.showSpeed()
print()

sportCar = SportCar(180, 'red', 'Katyusha')
sportCar.go()
sportCar.turn('left')
sportCar.stop()
sportCar.showSpeed()
print()
