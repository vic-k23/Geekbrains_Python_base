# Задание №4.
# Пользователь вводит целое положительное число.
#
# Найдите самую большую цифру в числе.
#
# Для решения используйте цикл while и арифметические операции.

# num = abs(int(input("Enter a number: ")))
num = -1
while num <= 0:
    num = int(input("Введите целое положительное число: "))
max = -1
pow = 1

while num // pow > 0:
    pow *= 10
    digit = (num % pow) // (pow // 10)
    if digit > max:
        max = digit
print(f"Самая большая цифра в числе {num} равна {max}")
