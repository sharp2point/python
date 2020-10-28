# 1.Реализовать класс «Дата»,  функция-конструктор которого
# должна принимать дату в виде строки формата «день-месяц-год».

class MyData:

    def __init__(self, inp_data: str):
        self._data_str = inp_data

    @classmethod
    def data_to_int(cls, data_str):
        data_list = list(map(int, data_str.split("-")))
        cls._int_dict = {"day": data_list[0],
                         "month": data_list[1],
                         "year": data_list[2]}
        return cls._int_dict

    @staticmethod
    def valid_data(inp_data_dict: dict):
        resp_str = ""
        is_data = True
        is_leap_year = True if inp_data_dict["year"] % 4 == 0 else False  # високосный год?
        is_30_day = {inp_data_dict["month"]}.issubset({4, 6, 9, 11})  # месяц с количеством дней 30?
        is_31_day = {inp_data_dict["month"]}.issubset({1, 3, 5, 7, 8, 10, 12})  # месяц с количеством дней 30?
        is_leap_month = inp_data_dict["month"] == 2  # февраль ?

        def is_verify(num, min_n, max_n):  # функция проверки диапазона
            if min_n <= num <= max_n:
                return True
            else:
                return False

        is_year = is_verify(inp_data_dict["year"], 0, 9999)
        is_month = is_verify(inp_data_dict["month"], 1, 12)
        is_day = False

        if is_30_day:
            is_day = is_verify(inp_data_dict["day"], 1, 30)
        elif is_31_day:
            is_day = is_verify(inp_data_dict["day"], 1, 31)

        if is_leap_month:  # февраль
            if is_leap_year:  # високосный год
                resp_str += " високосный год"
                is_day = is_verify(inp_data_dict["day"], 1, 29)
            else:
                is_day = is_verify(inp_data_dict["day"], 1, 28)

        if not is_day:
            resp_str += " \033[31m,ДЕНЬ\033[30m"
            is_data = False
        if not is_month:
            resp_str += " \033[31m,МЕСЯЦ\033[30m"
            is_data = False
        if not is_year:
            resp_str += " \033[31m,ГОД\033[30m"
            is_data = False

        return is_data, resp_str

    data_str = property()

    @data_str.getter
    def data_str(self):
        return self._data_str


# Использование класса и его методов
# Данные для проверки
data_list = [
    "30-11-2021",  # простой год
    "29-02-2000",  # високосный год
    "29-02-2001",  # високосный год , ошибка ДЕНЬ
    "32-11-2021",  # простой год , ошибка ДЕНЬ
    "02-13-1901",  # простой год , ошибка МЕСЯЦ
    "32-13-10901"  # простой год , ошибка ДЕНЬ МЕСЯЦ ГОД
]


def verify_data(data):
    data = MyData(data)
    data_dict = MyData.data_to_int(data.data_str)
    is_data = MyData.valid_data(data_dict)
    print("*-" * 30)
    if is_data[0]:
        print(f"{data_dict} Дата верна {is_data[1]}")
    else:
        print(f"{data_dict} Ошибка ввода даты {is_data[1]}")
    print("\n")


print(list(map(verify_data, data_list)))
