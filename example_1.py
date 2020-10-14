# 1. Реализовать скрипт, в котором должна быть предусмотрена
# функция расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
# (выработка в часах * ставка в час) + премия

from sys import argv


def employes_salary(prod_hour=0, rate=0, bonus=0):
    return prod_hour * rate + bonus


print(f"Зарплата сотрудника: {employes_salary(*list(map(float, argv[1::])))}")
