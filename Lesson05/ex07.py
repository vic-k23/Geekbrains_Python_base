# Задание №7
# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

from json import dump
from logging import getLogger, FileHandler

log = getLogger(__name__)
log.addHandler(FileHandler(f"{__name__}.log", encoding="UTF-8", delay=True))

try:
    with open("ex07_data.txt", "r", encoding="UTF-8") as f, open("ex07_output.json", "w", encoding="UTF-8") as f_out:
        firms_profit = {name: float(proceeds) - float(cost) for name, form, proceeds, cost in [l.split() for l in f]}
        average_profit = 0
        count = 0
        for i in [val for val in firms_profit.values() if val > 0]:
            average_profit +=i
            count += 1
        average_profit = {"average_profit": average_profit / count}
        dump([firms_profit, average_profit], f_out)
except IOError as io_err:
    log.error("Ошибка работы с файлом! Error #%d: %s", *io_err.args)
except Exception as other_err:
    log.error("Error: %s", other_err.args)