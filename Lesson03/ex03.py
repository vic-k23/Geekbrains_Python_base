# Задание №3
# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def sum_of_max(op1, op2, op3):
    return op2 + op3 if op1 < op2 and op1 < op3 else (op1 + op3 if op2 < op3 and op2 < op1 else op2 + op1)


numbers = [5, 4, 10]
print(sum_of_max(*numbers))
