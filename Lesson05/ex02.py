# Задание №2
# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

from logging import getLogger, FileHandler

log = getLogger(__name__)
log.addHandler(FileHandler(f"{__name__}.log", encoding="UTF-8", delay=True))

try:
    with open("user_input.txt", "r", encoding="UTF-8") as f:
        words_per_line = [len(line.split()) for line in f]
        print(f"В файле {len(words_per_line)} строк")
        print(f"Количество слов в строках: {words_per_line}")
except IOError as io_err:
    log.error("Ошибка работы с файлом! Error #%d: %s", *io_err.args)
except Exception as other_err:
    log.error("Error: %s", other_err.args)

