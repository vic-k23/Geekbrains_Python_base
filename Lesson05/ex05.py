# Задание №5
# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from logging import getLogger, FileHandler
from random import randint

log = getLogger(__name__)
log.addHandler(FileHandler(f"{__name__}.log", encoding="UTF-8", delay=True))

try:
    with open("ex05_file.txt", "w+", encoding="UTF-8") as f:
        for n in [randint(1, 30) for i in range(10)]:
            f.write(f"{n} ")
        summ = 0
        f.seek(0)
        for num in f.read().split():
            summ += int(num)
        print(f"Сумма чисел в файле равна: {summ}")
except IOError as io_err:
    log.error("Ошибка работы с файлом! Error #%d: %s", *io_err.args)
except Exception as other_err:
    log.error("Error: %s", other_err.args)
