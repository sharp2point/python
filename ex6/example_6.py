# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает
# учебный предмет и наличие лекционных, практических и лабораторных занятий по этому
# предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все
# типы занятий. Сформировать словарь, содержащий название предмета и общее количество
# занятий по нему. Вывести словарь на экран.

from io import open


def filter_digit_on_str(input_str: str) -> int:
    """
    Функция получает число из строки
    :param input_str: строка
    :return: вернуть число либо 0
    """
    tmp_str = ""
    for i in input_str:
        if i.isdigit():
            tmp_str += i
    if tmp_str.isdigit():
        return int(tmp_str)
    else:
        return 0


def read_file_to_list(file_name: str) -> list:
    """
    Функция подключается к файлу и возвращает список значений
    :param file_name: имя файла
    :return: список значений
    """
    with open(file_name, "r", encoding="utf-8") as file_handl:
        input_lst = file_handl.readlines()

        pred_lst = []
        for i in input_lst:
            pred_lst.append(i.split())

    return pred_lst


def present_dict(input_lst: list) -> dict:
    """
    Функция возвращает итоговый словарь
    :param input_lst:
    :return:
    """
    total_dict = {}
    for i in input_lst:
        sum = 0
        for j in i:
            k = filter_digit_on_str(j)
            sum += k
        total_dict.update({i[0]: sum})

    return total_dict


#-------------------------  Work  ----------------------------------------

total_dict = present_dict(read_file_to_list("test.txt"))

print(total_dict)
