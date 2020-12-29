# Задание №3
# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
# список только числами. Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
# скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список с числами выводится
# на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
# только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить
# соответствующее сообщение. При этом работа скрипта не должна завершаться.

class DigitValidatorError(Exception):
    def __init__(self, **kwargs):
        kwargs_keys = kwargs.keys()
        if "txt" in kwargs_keys:
            self.txt = kwargs["txt"]
        if "element" in kwargs_keys:
            self.element = kwargs["element"]
            self.txt = f"{self.element} типа {type(self.element)} не является числом."


class DigitValidator:
    @staticmethod
    def validate_list(lst):
        if type(lst) != list:
            raise TypeError(f"Ожидается список, передан {type(lst)}")
        else:
            for el in lst:
                if type(el) != int and type(el) != float:
                    raise DigitValidatorError(txt=f"В списке присутствует тип {type(el)}, который не является числом.")
            return True

    @staticmethod
    def validate_digit(el):
        try:
            if type(el) == int or type(el) == float:
                return el
            elif type(el) == str:
                negative = False
                if el[0] == "-":
                    negative = True
                    el = el.lstrip('-')
                if el.isdigit():
                    return int(el) * -1 if negative else int(el)
                elif el.find('.') >= 0:
                    el_parts = el.split('.')
                    if el_parts[0].isdigit() and el_parts[1].isdigit():
                        return float(".".join([el_parts[0], el_parts[1]])) * -1 if negative else float(".".join([el_parts[0], el_parts[1]]))
                    else:
                        raise DigitValidatorError(element=el)
                else:
                    raise DigitValidatorError(element=el)
            else:
                raise DigitValidatorError(element=el)
        except DigitValidatorError as dv_err:
            print(dv_err.txt)
            return False


if __name__ == '__main__':
    my_list = []
    while True:
        item = input("Введите элемент списка (stop - для завершения ввода): ")
        if item == "stop":
            break
        item = DigitValidator.validate_digit(item)
        if item != 0 and item:
            my_list.append(item)

    if DigitValidator.validate_list(my_list):
        print(my_list)
