# Задача №1
# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
# и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, str_date):
        self.__str_date = str_date

    @classmethod
    def decompose(cls, str_date):
        parts_list = str_date.split('-')
        parts = {"day": int(parts_list[0]), "month": int(parts_list[1]), "year": int(parts_list[2])}
        return parts

    @staticmethod
    def validate(str_date):
        parts_list = str_date.split('-')
        parts = {"day": int(parts_list[0]), "month": int(parts_list[1]), "year": int(parts_list[2])}
        if parts["day"] < 1 or (parts["day"] > 28 and parts["month"] == 2 and parts["year"] % 4 == 0) \
                            or (parts["day"] > 29 and parts["month"] == 2 and parts["year"] % 4 != 0) \
                            or (parts["day"] > 30 and parts["month"] in [4, 6, 9, 11]) \
                            or (parts["day"] > 31 and parts["month"] in [1, 3, 5, 7, 8, 10, 12]) \
                            or parts["month"] < 1 or parts["month"] > 12 \
                            or parts["year"] < 0:
            return False
        else:
            return True
