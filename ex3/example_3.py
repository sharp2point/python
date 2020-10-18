# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
# и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

from io import open


def min_profit_test(test_lst: list):
    """
    Функция поиска зарплат менее 20
    :param test_lst:
    :return: возвращает либо имя либо False
    """
    if int(test_lst[1]) < 20:
        return test_lst[0]
    else:
        return False

def all_calc_profit(empl_lst: list):
    """
    Функция подсчета среднего дохода
    :param empl_lst: список сотрудников
    :return: средний доход
    """
    average_profit = 0
    for i in lst:
        name_empl = min_profit_test(i)
        average_profit += int(i[1])
        if name_empl:
            print(f"{name_empl} - имеет доход менее 20")
    average_profit = average_profit/len(lst)
    print("* "*30 )
    return average_profit

def read_test_file(file_name: str) -> list:
    with open(file_name, "r", encoding="utf-8") as file_handl:
        out_lst = []
        for i in file_handl.readlines():
            out_lst.append(i.split())
        return out_lst


# ------------ Work ---------------------------------

lst = read_test_file("test.txt")

print(f"Средний доход: {all_calc_profit(lst):.4}")
