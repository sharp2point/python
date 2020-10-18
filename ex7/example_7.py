# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Итоговый список сохранить в виде json-объекта в соответствующий файл.


from io import open
from functools import reduce
import json

def profit_calc(input_data_list: list) -> dict:
    """
    :param input_data_list: список атрибутов
    :return: словарь key - названия фирмы : value - доход
    """
    data_key = input_data_list[0]
    data_item = float(input_data_list[1]) - float(input_data_list[2])
    return {data_key:data_item}

def data_parse(data_str: str):
    """
    :param data_str: Строка атрибутов
    :return: список из строки атрибутов
    """
    data_list = data_str.strip(".\n").split()
    data_list.pop(1)
    return data_list

def data_prepare(input_data_list: list) -> list:
    """
    :param input_data_list: Необработанный список значений
    :return: Итоговый лист
    """
    data_list = list(map(data_parse, input_data_list))
    data_list = list(map(profit_calc,data_list))

    # объеденяет словари фирм
    firm_dict = {}
    for i in data_list:
        firm_dict.update(i)

    # подсчитывает среднее значение прибыли
    average_profit = reduce(lambda x, y: x+y if y > 0 else x ,firm_dict.values())/len(firm_dict)

    # итоговый список
    total_list = [firm_dict,{"average_profit": average_profit}]
    return total_list

def read_data_file(data_file: str) -> list:
    """
    Функция чтения файла данных
    :param data_file: Путь к файлу с данными
    :return: Список полученных данных
    """
    with open(f"{data_file}", 'r', encoding='utf-8') as file_handle:
        print(f"Открыт файл для чтения: {file_handle.name}")
        return file_handle.readlines()

def data_to_json(file_json: str, total_list: list) -> json:
    with open(f"{file_json}","w") as file_handle:
        json.dump(total_list,file_handle)
        print(f"Файл {file_json} создан")


# ---- Work ----#
# прочитать файл
input_list = read_data_file("test.txt")
# подготовить данные
total_list = data_prepare(input_list)
print(total_list)
# сохранение данных в json
data_to_json("test_json.json",total_list)

