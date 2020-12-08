# Задание №1
# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(dividend, divider):
    """
    Функция принимает два параметра и возвращает частное от первого параметра на второй
    :param dividend: Делимое
    :param divider: Делител
    :return: Частное
    """
    try:
        return float(dividend) / float(divider)
    except ValueError:
        print("Не числовой операнд!")
        return None
    except ZeroDivisionError:
        print("Ошибка! Деление на ноль!")


str_div_operands = ""
while len(str_div_operands) == 0:
    str_div_operands = input("Введите операнды деления по одному либо через пробел: ")

operands = str_div_operands.split()
if len(operands) >= 2:
    print(f"{operands[0]} / {operands[1]} = {division(operands[0], operands[1])}")
else:
    operands.append(input("Введите делитель: "))
    print(f"{operands[0]} / {operands[1]} = {division(operands[0], operands[1])}")
