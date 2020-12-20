# Задача №2
# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
# одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
# V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def __init__(self, name, parameter):
        pass

    @property
    @abstractmethod
    def model(self):
        pass

    @property
    @abstractmethod
    def size_parameter(self):
        pass

    @size_parameter.setter
    @abstractmethod
    def size_parameter(self, value):
        pass

    @property
    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, name: str, width: int):
        self.__name = str(name)
        self.__width = 0
        self.size_parameter = width

    @property
    def model(self):
        return self.__name

    @property
    def size_parameter(self):
        return self.__width

    @size_parameter.setter
    def size_parameter(self, value: int):
        if value < 30:
            self.__width = 30
        elif value > 58:
            self.__width = 58
        else:
            self.__width = value

    @property
    def fabric_consumption(self):
        return self.__width / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, name: str, height: int):
        self.__name = str(name)
        self.__height = 0
        self.size_parameter = height

    @property
    def model(self):
        return self.__name

    @property
    def size_parameter(self):
        return self.__height

    @size_parameter.setter
    def size_parameter(self, value: int):
        if value < 30:
            self.__height = 30
        elif value > 250:
            self.__height = 250
        else:
            self.__height = value

    @property
    def fabric_consumption(self):
        return self.__height * 2 + 0.3

