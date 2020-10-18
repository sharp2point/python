# 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле
# и выводить ее на экран.

from io import open
from functools import reduce

num_lst = [1, 2, 3, 4, 5]


def create_file(file_name: str):
    with open(file_name, "w", encoding="utf-8") as file_handl:
        for i in num_lst:
            file_handl.write(f"{i} ")


def read_file_to_sum(file_name: str) -> int:
    with open(file_name, "r", encoding="utf-8") as file_handl:
        return reduce(lambda x, y: int(x) + int(y), file_handl.read().split())


# ---------- Work -----------------------------------------------------------
create_file("test.txt")
print(read_file_to_sum("test.txt"))
