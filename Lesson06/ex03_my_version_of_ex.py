# Задача №3
# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность).
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
# (get_total_income) и поля оклад и премия.
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

class Position:
    def __init__(self, name, wage, bonus):
        self.name = name
        self.income = {"wage": wage, "bonus": bonus}

    def get_total_income(self):
        return self.income["wage"] + self.income["bonus"]

    def get_position_name(self):
        return self.name


class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = position.income

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_worker_income(self):
        return self._income


pos = Position("Администратор", 15000, 10000)
worker = Worker("Иван", "Тюмеров", pos)
print(worker.get_worker_income())
print(worker.get_full_name())
print(worker.position.get_position_name())
print(worker.position.get_total_income())
