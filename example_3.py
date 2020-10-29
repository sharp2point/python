# 3.Создайте собственный класс-исключение, который должен проверять содержимое
# списка на наличие только чисел. Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список только числами.
# Класс-исключение должен контролировать типы данных элементов списка.

class NotIntException(ValueError):

    def __init__(self, txt, val):
        self.val = txt

    def __str__(self):
        return self.val


# --------------------------------------------
global_lst = list()


def input_test():
    input_str = input("Вводите числа:")
    if input_str == "stop":
        return 0
    try:
        if not input_str.isdigit():
            raise NotIntException("Только числа", input_str)
        else:
            global_lst.append(float(input_str))
            return 1

    except NotIntException as nie:
        print(f"{nie}, <{nie.args[1]}> -> не число")
        return 1


# ----------------------------------------------------------------
while input_test():
    input_test()
else:
    print("\n Список чисел:")
    print(global_lst)
