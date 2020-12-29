# Задание №2
# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.

from random import randint

initial_list = [randint(-100, 100) for i in range(33)]

result_list = [val for idx, val in initial_list if val > initial_list[idx-1]]
print(result_list)
