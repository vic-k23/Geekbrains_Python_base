# Задача №4+5+6
# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, копир).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать
# любую подходящую структуру, например словарь. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
from abc import ABC, abstractmethod
from math import ceil
from time import sleep
from re import findall


class Stock:
    """Класс Склад содержит объекты Стеллаж."""
    def __init__(self):
        """
        Инициализатор создаёт склад
        """
        """Словарь типов оборудования, помещённого когда-либо на этот склад, с указанием количества."""
        self.__equipment = {}

    def push_equipment(self, equipment, count=1):
        """
        Функция размещает оборудование на склад.
        :param count: Количество помещаемой техники
        :param equipment: Оборудование, размещаемое на склад
        :return: None
        """
        if str(equipment) in self.__equipment.keys():
            self.__equipment[str(equipment)] += count
        else:
            self.__equipment[str(equipment)] = count

    def count_equipment(self, equipment: str):
        """
        Вычисляет количество техники определённого в параметре типа
        :param equipment: Строкове представление класса оргтехники
        :return: Возвращает количество оргтехники запрошенного типа на всём складе
        """

        if equipment in self.__equipment.keys():
            return self.__equipment[equipment]
        else:
            return 0

    def pop_equipment(self, equipment: str, count=1):
        """
        Выдать со склада технику.
        :param count: количество выдаваемой техники
        :param equipment: строковое представление класса требуемой оргтехники
        :return: кортеж, состоящий из объекта оргтехники требуемого типа и количества,
                либо пустой кортеж, если некорректно задано имя класса,
                либо кортеж с сообщением о недостаточном количестве с указанием недостающего количества
                либо кортеж (None, 0), если такой техники нет на складе
        """
        if equipment in self.__equipment.keys():
            if self.__equipment[equipment] >= count:
                self.__equipment[equipment] -= count
                cls_name = equipment[:equipment.find(' ')]
                params = equipment[equipment.find(' ') + 1:]
                manufacturer, model, performance, interfaces, color = params.split('/')
                interfaces = findall("[A-Za-z]+", interfaces)
                if cls_name == "Printer":
                    return Printer(manufacturer, model, performance, interfaces, color), count
                elif cls_name == "Scanner":
                    return Scanner(manufacturer, model, performance, interfaces, color), count
                elif cls_name == "Copier":
                    return Copier(manufacturer, model, performance, interfaces, color), count
                else:
                    return ()
            else:
                return f"Не хватает {count - self.__equipment[equipment]} единиц", self.__equipment[equipment] - count
        else:
            return None, 0

    def equipment_list(self):
        return self.__equipment


class Equipment(ABC):
    """Базовый класс для оргтехники"""

    @staticmethod
    @abstractmethod
    def stringify_me(manufacturer, model, performance, interfaces, color):
        """Метод должен реализовывать тот же функционал, что и __str__"""
        pass

    def __init__(self, manufacturer: str, model: str, performance: float, interfaces: list, color: str):
        """
        Initializer
        :param manufacturer: manufacturer of a printer manufacturer
        :param color: Color of the printer
        :param model: Model of the printer
        :param performance: performance in pages per minute
        :param interfaces: available interfaces for connection
        """
        self.__manufacturer = str(manufacturer)
        self.__color = str(color)
        self.__model = str(model)
        self.__performance = float(performance)
        self.__interfaces = list(interfaces)

    @property
    def manufacturer(self):
        """Returns the manufacturer of an equipment"""
        return self.__manufacturer

    @property
    def color(self):
        """Returns the color of an equipment"""
        return self.__color

    @property
    def model(self):
        """Returns the model of an equipment"""
        return self.__model

    @property
    def performance(self):
        """Returns the performance of an equipment"""
        return self.__performance

    @property
    def interfaces(self):
        """Returns the performance of an equipment"""
        return self.__interfaces


class Printer(Equipment):
    """Class Printer describes printer"""
    @staticmethod
    def stringify_me(manufacturer, model, performance, interfaces, color):
        """
        Используется для создания строкового предтавления экземпляра класса без создания самого экземпляра.
        Применяется для запроса техники со склада
        :param manufacturer: manufacturer of a printer manufacturer
        :param color: Color of the printer
        :param model: Model of the printer
        :param performance: performance in pages per minute
        :param interfaces: available interfaces for connection
        :return: Строковое представления экземпляра класса
        """
        return f"Printer {manufacturer}/{model}/{float(performance)}/{interfaces}/{color}"

    def __init__(self, manufacturer, model, performance, interfaces, color):
        super().__init__(manufacturer, model, performance, interfaces, color)
        self.__paper_storage = 0

    def __str__(self):
        return f"Printer {self.manufacturer}/{self.model}/{self.performance}/{self.interfaces}/{self.color}"

    def put_paper(self, pages_count):
        """Функция добавляет бумагу в принтер"""
        self.__paper_storage += pages_count

    def print(self, pages_count, duplex):
        """
        Функция печати
        :param pages_count: Количество печатаемых страниц
        :param duplex: Флаг двусторонней печати (нужен для подсчёта использованных страниц)
        :return: None
        """
        if (not duplex and self.__paper_storage < pages_count) or (duplex and self.__paper_storage < pages_count / 2):
            print("Not enough paper!")
        else:
            self.__paper_storage -= ceil(pages_count / 2) if duplex else pages_count
            print("Printing...")
            sleep(pages_count / self.performance * 60)
            print("Finished successfully!")


class Scanner(Equipment):
    """
    Класс Сканер
    """

    @staticmethod
    def stringify_me(manufacturer: str, model: str, performance: float, interfaces: list, color: str):
        """
        Используется для создания строкового предтавления экземпляра класса без создания самого экземпляра.
        Применяется для запроса техники со склада
        :param manufacturer: manufacturer of a Scanner
        :param color: Color of the Scanner
        :param model: Model of the Scanner
        :param performance: performance in pages per minute
        :param interfaces: available interfaces for connection
        :return: Строковое представления экземпляра класса
        """
        return f"Scanner {manufacturer}/{model}/{float(performance)}/{interfaces}/{color}"

    def __init__(self, manufacturer, model, performance, interfaces, color):
        super().__init__(manufacturer, model, performance, interfaces, color)

    def __str__(self):
        return f"Scanner {self.manufacturer}/{self.model}/{self.performance}/{self.interfaces}/{self.color}"

    def scan(self, pages_count):
        """
        Функция сканирования
        :param pages_count: Количество сканируемых странци (нужно для подсчёта задержки при иммитации действия)
        :return: None
        """
        print("Scanning...")
        sleep(pages_count / self.performance * 60)
        print("Saving result...")
        sleep(3)
        print("Finished successfully!")


class Copier(Printer, Scanner):
    """Класс Копир"""

    @staticmethod
    def stringify_me(manufacturer, model, performance, interfaces, color):
        """
        Используется для создания строкового предтавления экземпляра класса без создания самого экземпляра.
        Применяется для запроса техники со склада
        :param manufacturer: manufacturer of a Copier
        :param color: Color of the Copier
        :param model: Model of the Copier
        :param performance: performance in pages per minute
        :param interfaces: available interfaces for connection
        :return: Строковое представления экземпляра класса
        """
        return f"Copier {manufacturer}/{model}/{float(performance)}/{interfaces}/{color}"

    def __init__(self, manufacturer, model, performance, interfaces, color):
        super().__init__(manufacturer, model, performance, interfaces, color)

    def __str__(self):
        return f"Copier {self.manufacturer}/{self.model}/{self.performance}/{self.interfaces}/{self.color}"

    def copy(self, pages_count, duplex=False):
        """
        Функция копирования
        :param duplex: Флаг двусторонней печати (нужен для подсчёта использованных страниц)
        :param pages_count: Количество страниц
        :return: None
        """
        super().scan(pages_count)
        super().print(pages_count, duplex)


if __name__ == "__main__":
    stock1 = Stock()
    printer1 = Printer("Hewlett Packard", "LaserJet P1000", 20, ["USB", "WiFi"], "black")
    scanner1 = Scanner("Canon", "Unknown", 3, ["USB"], "white")
    copier1 = Copier("Kyocera", "Ecosys 2035dn", 10, ["USB", "Ethernet"], "white")
    stock1.push_equipment(printer1, 10)
    stock1.push_equipment(printer1)
    stock1.push_equipment(scanner1, 5)
    stock1.push_equipment(copier1, 20)
    print(stock1.count_equipment(Printer.stringify_me("Hewlett Packard", "LaserJet P1000", 20, ["USB", "WiFi"], "black")))
    print(stock1.equipment_list())
    stock2 = Stock()
    scanner_mover = stock1.pop_equipment(Scanner.stringify_me("Canon", "Unknown", 3, ["USB"], "white"), 2)
    stock2.push_equipment(*scanner_mover)
    scanner_mover = stock1.pop_equipment(Scanner.stringify_me("Canon", "Unknown", 3, ["USB"], "white"), 1)
    stock2.push_equipment(*scanner_mover)
    stock2.push_equipment(*stock1.pop_equipment(Copier.stringify_me("Kyocera", "Ecosys 2035dn", 10, ["USB", "Ethernet"], "white"), 5))
    print(stock2.count_equipment(Scanner.stringify_me("Canon", "Unknown", 3, ["USB"], "white")))
    print(stock2.equipment_list())
    printer1.print(5, True)
    printer1.put_paper(100)
    printer1.print(5, True)
    copier1.put_paper(50)
    copier1.copy(2)
