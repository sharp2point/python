# 6. Реализовать два небольших скрипта:
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

from sys import argv
from itertools import cycle

try:
    arg_lst = list(argv[1:])
    iter_num = int(arg_lst[0])
    pattern_str = arg_lst[1:]
    if len(pattern_str) < 1 :
        raise Exception("Сишком мало параметров")
    print(f"Выводим значения списка {pattern_str}, {iter_num} раз")
except (ValueError,IndexError,Exception):
    print("Ошибка ввода!")
    iter_num = 3
    pattern_str = ["Hello", "Darling"]
    print(f"Выводим значения по умолчанию {pattern_str}, {iter_num} раз")

# функция принимает итеррируемый список pattern_str и колличество иттераций iter_num
def cycle_list(pattern_str=["Hello", "Darling"], iter_num = 3):
    iter_c = cycle(pattern_str)
    for i in range(iter_num):
        print(next(iter_c))


cycle_list(pattern_str,iter_num)
