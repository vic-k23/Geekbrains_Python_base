# Задание №2
# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.

class DivisionToZero(ZeroDivisionError):
    def __init__(self):
        self.txt = "На ноль делить нельзя, получим бесконечность."


def division(dividend, divisor):
    if divisor == 0:
        raise DivisionToZero()
    else:
        return dividend / divisor


if __name__ == '__main__':
    try:
        a = input("Введите делимое: ")
        b = input("Введите делитель: ")
        print(division(float(a), float(b)))
    except ValueError as v_err:
        print(v_err)
    except DivisionToZero as div_err:
        print(div_err.txt)
