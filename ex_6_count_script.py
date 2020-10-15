# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного

from sys import argv
from itertools import count

try:
    start_num, iter_num = argv[1:] or [1, 5]
    start_num = int(start_num)
    iter_num = int(iter_num)
except ValueError:
    start_num, iter_num = 1,5

# скрипт принимает начальное значение start_num
# и колличество итераций iter_num
def count_list(start_num=3, iter_num=10):
    iter_c = count(start_num)
    for i in range(iter_num):
        print(f"{i}. {next(iter_c)}")


count_list(start_num, iter_num)
