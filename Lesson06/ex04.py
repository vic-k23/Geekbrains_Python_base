# Задача №4
# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда)
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f"Машина повернула на{direction}")

    def show_speed(self):
        return self.speed


class WorkCar(Car):
    def __init__(self, speed, color, name, tonnage=3):
        super().__init__(speed, color, name, False)
        self.tonnage = tonnage

    def show_speed(self):
        speed = super().show_speed()
        return speed if speed <= 40 else f"Превышение скорости: {speed}!"


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        speed = super().show_speed()
        return speed if speed <= 60 else f"Превышение скорости: {speed}!"


class SportCar(Car):
    def __init__(self, speed, color, name, maxspeed=300, acceleration=5.0):
        super().__init__(speed, color, name, False)
        self.maxspeed = maxspeed
        self.acceleration = acceleration


class PoliceCar(Car):
    def __init__(self, speed, color, name, maxspeed=300, acceleration=5.0):
        super().__init__(speed, color, name, True)
        self.maxspeed = maxspeed
        self.acceleration = acceleration


tc = TownCar(0, "white", "Picanto")
wc = WorkCar(0, "grey", "Next")
sc = SportCar(0, "red", "Ferrari", acceleration=4.3)
pc = PoliceCar(0, "white-blue", "Camry")

sc.go()
sc.speed = 180
print(sc.show_speed())
print(sc.color)

pc.go()
pc.speed = 150
pc.turn("право")

tc.speed = 65
print(tc.show_speed())

wc.speed = 65
print(wc.show_speed())
