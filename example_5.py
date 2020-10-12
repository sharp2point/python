# Задание 5
# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и
# снова нажать Enter.

summa = 0.0  # Сумма чисел


def get_input() -> list:
    '''
    Принимает ввод пользователя
    :return: строковый лист
    '''
    input_lst = input("Введите числа через пробел:").split()
    return input_lst


def str_to_numb(input_str: str) -> tuple:
    '''
    :param input_str: Строка
    :return: Кортеж (Число, флаг выхода is_quit)
    is_quit - булева переменная реакция на ввод символа "q"
    '''
    if input_str == 'q':
        is_quit = True
        input_str = 0
    else:
        is_quit = False
        input_str = float(input_str)

    return input_str, is_quit


def sum_list(numb_lst: list) -> tuple:
    '''
    :param numb_lst: Числовой лист
    :return: Кортеж (сумма чисел листа, флаг выхода)
    '''
    insum = 0
    for i in numb_lst:
        if i[1]:
            return insum, True
        else:
            insum += i[0]
    return insum, False


# рабочий цикл
while True:
    tmp_tupl = sum_list(list(map(str_to_numb, get_input())))
    summa += tmp_tupl[0]
    if tmp_tupl[1]:  # Если False -> значит на вводе был символ "q"
        print(f"Общая сумма: {summa} . Ввод окончен!")
        break
    else:
        print(f"Промежуточная сумма: {summa} ")
