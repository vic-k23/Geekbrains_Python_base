# Задача №3
# Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
# вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()). Данные методы должны применяться только
# к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением до целого) деление клеток,
# соответственно...

class Cell:
    def __init__(self, slots_num: int):
        if slots_num <= 0:
            raise ValueError("Клетк не может быть пустой или отрицательной ёмкости!")
        else:
            self.slots = slots_num

    def __str__(self):
        return "*" * self.slots

    def __add__(self, other):
        return Cell(self.slots + other.slots)

    def __sub__(self, other):
        if self.slots == other.slots:
            raise ValueError("Нельзя вычитать равные по размеру клетки!")
        else:
            return Cell(self.slots - other. slots if self.slots > other.slots else other.slots - self.slots)

    def __mul__(self, other):
        return Cell(self.slots * other.slots)

    def __truediv__(self, other):
        return Cell(self.slots // other.slots)

    def make_order(self, row_length):
        begin = 0
        full_cell = str(self)
        result = [full_cell[begin:begin + row_length]]
        while begin + row_length < self.slots:
            begin += row_length
            result.append(full_cell[begin:begin + row_length])
        return "\n".join(result)


c = Cell(2)
print(c.make_order(3))
