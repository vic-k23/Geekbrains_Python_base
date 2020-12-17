# Задача №4
# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда)
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    pub_speed_limit = 0
    _prot_speed_limit = 0
    __priv_speed_limit = 0

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
    pub_speed_limit = 40
    _prot_speed_limit = 40
    __priv_speed_limit = 40

    def __init__(self, speed, color, name, tonnage=3):
        super().__init__(speed, color, name, False)
        self.tonnage = tonnage

    def show_speed(self):
        speed = super().show_speed()
        # return speed if speed <= self.__priv_speed_limit else f"TownCar: Превышение скорости {__priv_speed_limit}!"
        # return speed if speed <= self.pub_speed_limit else f"TownCar: Превышение скорости {pub_speed_limit}!"
        # return speed if speed <= self._prot_speed_limit else f"TownCar: Превышение скорости {_prot_speed_limit}!"
        return speed if speed <= self.__priv_speed_limit else f"TownCar: Превышение скорости {self.__priv_speed_limit}!"
        # return speed if speed <= self.pub_speed_limit else f"TownCar: Превышение скорости {self.pub_speed_limit}!"
        # return speed if speed <= self._prot_speed_limit else f"TownCar: Превышение скорости {self._prot_speed_limit}!"


class TownCar(Car):
    pub_speed_limit = 60
    _prot_speed_limit = 60
    __priv_speed_limit = 60

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        speed = super().show_speed()
        return speed if speed <= self.__priv_speed_limit else f"TownCar: Превышение скорости {__priv_speed_limit}!"
        # return speed if speed <= self.pub_speed_limit else f"TownCar: Превышение скорости {pub_speed_limit}!"
        # return speed if speed <= self._prot_speed_limit else f"TownCar: Превышение скорости {_prot_speed_limit}!"
        # return speed if speed <= self.__priv_speed_limit else f"TownCar: Превышение скорости {self.__priv_speed_limit}!"
        # return speed if speed <= self.pub_speed_limit else f"TownCar: Превышение скорости {self.pub_speed_limit}!"
        # return speed if speed <= self._prot_speed_limit else f"TownCar: Превышение скорости {self._prot_speed_limit}!"


class SportCar(Car):
    def __init__(self, speed, color, name, maxspeed=300, acceleration=5.0):
        super().__init__(speed, color, name, False)
        self.maxspeed = maxspeed
        self.acceleration = acceleration
        self.speed_limit = maxspeed


class PoliceCar(Car):
    def __init__(self, speed, color, name, maxspeed=300, acceleration=5.0):
        super().__init__(speed, color, name, True)
        self.maxspeed = maxspeed
        self.acceleration = acceleration


wc = WorkCar(0, "grey", "Next")
wc.speed = 65
print(wc.show_speed())

# Ответ на вызов:
# Если в классе наследник переопределить поля родителя, то при обращении к таким полям мы, очевидно, обращаемся именно к
# переопределённым полям наследника. При этом у нас есть доступ (в моём варианте) даже к приватному полю, потому что
# внутри класса оно, как и положено, доступно, пока мы не обратимся к нему через объект напрямую. Если же
# не переопределять, то обращаться мы будем к полям родителя и получим соответствующие значения,
# определённые в родителе. При этом, разумеется, даже в методах потомка нет доступа к приватному полю родителя,
# но есть доступ к защищённому (protected). Надеюсь, я смог понять задачу вызова. ))
