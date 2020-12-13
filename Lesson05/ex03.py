# Задание №3
# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

from logging import getLogger, FileHandler

log = getLogger(__name__)
log.addHandler(FileHandler(f"{__name__}.log", encoding="UTF-8", delay=True))

try:
    with open("employers.txt", "r", encoding="UTF-8") as f:
        words_per_line = [line.split()[0] for line in f if float(line.split()[1]) < 20000]
        print(f"Сотрудники с окладом менее 20 тыс.: {words_per_line}")
except IOError as io_err:
    log.error("Ошибка работы с файлом! Error #%d: %s", *io_err.args)
except Exception as other_err:
    log.error("Error: %s", other_err.args)
