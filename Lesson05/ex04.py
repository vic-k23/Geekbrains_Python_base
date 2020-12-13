# Задание №4
# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться
# в новый текстовый файл.


from logging import getLogger, FileHandler

log = getLogger(__name__)
log.addHandler(FileHandler(f"{__name__}.log", encoding="UTF-8", delay=True))

try:
    with open("ex04_resource.txt", "r", encoding="UTF-8") as f_in, open("ex04_output.txt", "w", encoding="UTF-8") as f_out:
        translate = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
        for l in f_in:
            f_out.write(f"{l.replace(l[:l.find(' ')], translate[l[:l.find(' ')]])}\n")
except IOError as io_err:
    log.error("Ошибка работы с файлом! Error #%d: %s", *io_err.args)
except Exception as other_err:
    log.error("Error: %s", other_err.args)