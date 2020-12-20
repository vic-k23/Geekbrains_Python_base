# Задача №2
# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу:
#
# длина * ширина
#   * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см
#   * число см толщины полотна.
#
# Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 125 т

class Road:
    def __init__(self, lng, w):
        self._length = lng
        self._width = w

    def asphalt_weight(self, r, h, lng=None, w=None):
        if lng is None:
            lng = self._length
        if w is None:
            w = self._width
        return lng * w * r * h


road = Road(20, 5000)
print(f"road.asphalt_weight(0.025, 0.05) т")
