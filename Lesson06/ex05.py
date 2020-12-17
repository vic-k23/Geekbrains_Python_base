# Задача №5
# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
# и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.

class Stationery:
    title = "stationary"

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    # Переопределяем метод родителя
    def draw(self):
        print("Так пишет ручка")


class Pencil(Stationery):
    # Переопределяем метод родителя
    def draw(self):
        print("Так пишет карандаш")


class Handle(Stationery):
    # Переопределяем метод родителя
    def draw(self):
        print("Так пишет маркер")


stationery = Stationery()
pen = Pen()
pencil = Pencil()
handle = Handle()

stationery.draw()
pen.draw()
pencil.draw()
handle.draw()
