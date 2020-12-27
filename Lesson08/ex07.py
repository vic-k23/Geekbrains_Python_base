# Задача №7
# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса
# (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Complex:
    """Класс Комлексное число"""
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return Complex(self.a * other.a - self.b * other.b, self.b * other.a + self.a * other.b)

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    def __str__(self):
        if self.b > 0:
            return f"{self.a} + {self.b}i"
        elif self.b == 0:
            return self.a
        else:
            return f"{self.a} - {self.b * -1}i"


if __name__ == "__main__":
    m = Complex(2, -3)
    n = Complex(5, 7)
    print(m + n)
    print(m * n)
