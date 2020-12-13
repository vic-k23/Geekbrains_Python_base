# Задание №1
# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open("user_input.txt", "w", encoding='UTF-8') as file:
    user_input = "text"
    while True:
        user_input = input("> ")
        if user_input == "":
            break
        file.write(f"{user_input}\n")
