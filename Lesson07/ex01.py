# Задача №1
# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса
# Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, mtx_lst):
        if type(mtx_lst) != list:
            raise TypeError(f"Необходимо передать список в качестве инициализирующего параметра! {type(mtx_lst)} был передан")
        else:
            self.mtx = mtx_lst
            self.rows = len(mtx_lst)
            if type(self.mtx[0]) == list:
                self.cols = len(self.mtx[0])
            else:
                self.cols = 0
            for i in range(1, self.rows):
                if type(self.mtx[i]) == list and self.cols != len(self.mtx[i]):
                    raise ValueError("Размерность массива рванная, ряды не одинаковой длины!")

    def __str__(self):
        if self.cols > 0:
            str_mtx = "{}\n" * self.rows
            return str_mtx.format(*self.mtx)
        else:
            return f"{self.mtx}"

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Нельзя складывать матрицы разной размерности!")
        result = []
        for i in range(0, self.rows):
            if self.cols > 0:
                line = []
                for j in range(0, self.cols):
                    line.append(self.mtx[i][j] + other.mtx[i][j])
                result.append(line)
            else:
                result.append(self.mtx[i] + other.mtx[i])
        return Matrix(result)

