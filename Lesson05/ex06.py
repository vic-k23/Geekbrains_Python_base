# Задание №6
# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета
# не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий
# по нему.
# Вывести словарь на экран.

from logging import getLogger, FileHandler

log = getLogger(__name__)
log.addHandler(FileHandler(f"{__name__}.log", encoding="UTF-8", delay=True))


def get_hours_sum(str_columns):
    s = 0
    try:
        for i in str_columns.split():
            if i[:i.find("(")] != '':
                s += int(i[:i.find("(")])
        return s
    except ValueError as v_err:
        log.error("Неверный аргумент: %s", v_err.args)
        return 0


try:
    with open("ex06_data.txt", "r", encoding="UTF-8") as f:
        courses = {}
        for subj in f.readlines():
            rec = subj.split(":")
            courses[rec[0]] = get_hours_sum(rec[1])
        print(courses)
except IOError as io_err:
    log.error("Ошибка работы с файлом! Error #%d: %s", *io_err.args)
except Exception as other_err:
    log.error("Error: %s", other_err.args)
