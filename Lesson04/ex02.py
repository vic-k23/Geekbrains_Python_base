# Задание №2
# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.

from random import randint

initial_list = [randint(-100, 100) for i in range(33)]
print("Исходный список:")
print(initial_list)
prev = initial_list[0]
# В задании не указано, что делать с первым элементом, поэтому просто перепишем его в результирующий список
result_list = list([initial_list[0]])
for i in initial_list:
    if i > prev:
        result_list.append(i)
    prev = i
print("Результрующий список:")
print(result_list)
