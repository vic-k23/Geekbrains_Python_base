# Задание №3.
# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

str_n = input("Введите число: ")
n = int(str_n)
nn = int(f"{str_n}{str_n}")
nnn = int(f"{str_n}{str_n}{str_n}")

print(n, nn, nnn)
print(n + nn + nnn)
