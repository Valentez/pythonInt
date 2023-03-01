"""
4. Реализуйте базовый класс Car.

    у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
    опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
    добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
    для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.
"""


class Cars:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print("Привет!")

    def go(self):
        print(f"Машина {self.color} цвета, марки {self.name} поехала со скоростью {self.speed}")

    def stop(self):
        print(f"Машина {self.color} цвета, марки {self.name} остановилась")

    def turn(self, direction):
        print(f"Машина {self.color} цвета, марки {self.name} повернула на{direction}")

    def show_speed(self):
        print(f"Текущая скорость машины {self.speed}")


class TownCar(Cars):
    # def __init__(self, speed, color, name, is_police):
    #     Cars.__init__(self, speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print("Превышение скорости! Замедлите ход!")
        else:
            Cars.show_speed(self)


class SportCar(Cars):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=False)


class WorkCar(Cars):
    # def __init__(self, speed, color, name, is_police):
    #     Cars.__init__(self, speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print("Превышение скорости! Замедлите ход!")


class PoliceCar(Cars):
    def __init__(self, speed, color, name):
        Cars.__init__(self, speed, color, name, is_police=True)


my_police_car = PoliceCar(90, "white", "Reno Megan")
my_police_car.go()
my_police_car.turn("лево")
my_police_car.stop()
my_police_car.show_speed()

work_car = WorkCar(85, "black", "Work Car", False)
work_car.go()
work_car.turn("лево")
work_car.stop()
work_car.show_speed()

sport_car = SportCar(250, "red", "Sport Car")
sport_car.go()
sport_car.turn("право")
sport_car.stop()
sport_car.show_speed()


