# 2.Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
# в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class DivOnZeroException(Exception):
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return "DivOnZeroException: " + self.val


# --------------------------------------------------------
def input_reader():
    try:
        input_numb = input("Введите делитель:")

        if input_numb == "q":  # если введено <q> выйти из программы
            print("Программа завершена !")
            exit()

        input_numb = float(input_numb)

        if input_numb == 0:
            raise DivOnZeroException("\033[31mНа ноль делить нельзя\033[30m")

        print(f"Результат деления: {1 / input_numb}")
        print("*-Продолжайте ввод" * 10)
        input_reader()

    except ValueError as ve:
        print(ve)
        print("*-Продолжайте ввод" * 10)
        input_reader()

    except DivOnZeroException as dz:
        print(dz)
        print("*-Продолжайте ввод" * 10)
        input_reader()


# --------------------------------------------
input_reader()
