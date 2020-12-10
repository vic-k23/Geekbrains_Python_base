# Задание №2
# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_profile(**kwargs):
    name = kwargs.get("name")
    surname = kwargs.get("surname")
    yob = kwargs.get("yob")
    city = kwargs.get("city")
    email = kwargs.get("email")
    phone = kwargs.get("phone")

    print(f"{name} {surname}, {yob} г.р. из г.{city}. Контакты: {email}, {phone}")


user = dict()
user["name"], user["surname"] = input("Введите Имя Фамилия пользователя: ").split()
user["yob"] = ""
while not user["yob"].isdigit() or len(user["yob"]) != 4:
    user["yob"] = input("Введите год рождения пользователя в формате NNNN: ")
user["city"] = input("Введите город проживания пользователя: ")
user["email"] = input("Введите e-mail пользователя: ")
while user["email"].find("@") < 0:
    print(f"{user['email']} - это неправильный формат e-mal!")
    user["email"] = input("Введите e-mail пользователя: ")
user["phone"] = input("Введите номер телефона пользователя в формате NNNNNNNNNNN: ")
while not user["phone"].isdigit() or len(user["phone"]) != 11:
    print(f"{user['phone']} - это неправильный формат номера!")
    user["phone"] = input("Введите номер телефона пользователя в формате NNNNNNNNNNN: ")

user_profile(**user)
