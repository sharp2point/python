# 7. Реализовать генератор с помощью функции с ключевым словом yield,
# создающим очередное значение. При вызове функции должен
# создаваться объект-генератор.
from functools import reduce


# Функция генератор
def range_yield(n):
    for i in range(0, n):
        yield i+1

# Функция вычисления факториала
def my_factorial(fy: iter):
    fact_list = []
    for i in fy:
        fact_list.append(i)

    print(f"{len(fact_list)}! = {'*'.join([str(i) for i in fact_list])} = {reduce(lambda x, y: x * y, fact_list)}")

# Рабочий цикл
while True:
    try:
        fact_input = input("Введите целое число:")
        if fact_input == 'q':
            print("Программа завершена.")
            break
        else:
            fact_input = int(fact_input)
            if fact_input == 0:
                raise Exception("Факториал 0!")
        my_factorial(range_yield(fact_input))
    except (ValueError, Exception):
        print("Ошибка ввода!")

