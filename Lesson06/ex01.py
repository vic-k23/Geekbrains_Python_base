# Задание №1
# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
# и завершать скрипт.

from time import sleep


class TrafficLight:
    __COLORS = {"red": 7, "yellow": 2, "green": 5}

    def __init__(self, c = "red"):
        self.__color = c
        print(self.__color)

    def running(self):
        if self.__color == "red":
            self.__color = "yellow"
        elif self.__color == "yellow":
            self.__color = "green"
        else:
            self.__color = "red"
        print(self.__color)

    def get_color(self):
        return self.__color

    def get_color_interval(self, c):
        return self.__COLORS[c]


tl = TrafficLight()
sleep(tl.get_color_interval(tl.get_color()))
tl.running()
sleep(tl.get_color_interval(tl.get_color()))
tl.running()
sleep(tl.get_color_interval(tl.get_color()))
