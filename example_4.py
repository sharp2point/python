# Задание №4
# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).

def get_x_num() -> float:
    '''
        Функция поьзовательского ввода возводимого в степень числа: x_num
    '''
    while True:
        try:
            x_num = float(
                input("Введите действительное число больше нуля :"))
            if x_num == 0:
                raise ZeroDivisionError
            break
        except (ValueError, ZeroDivisionError):
            print("Ошибка ввода ! Попробуйте ещё раз")
    return x_num


def get_y_num() -> int:
    '''
            Функция поьзовательского ввода степени числа: y_num
    '''
    while True:
        try:
            y_num = int(
                input("Введите отрицательную целую степень числа :"))
            if y_num > 0:
                raise Exception
            break
        except (ValueError, Exception):
            print("Ошибка ввода ! Попробуйте ещё раз")
    return y_num


def my_func(x: float, y: int) -> float:
    '''  Функция возведения действительного числа
         в целую отрицатеьную степень через оператор ** '''
    return x ** y


def my_func_2(x: float, y: int) -> float:
    '''  Функция возведения действительного числа
         в целую отрицатеьную степень через цикл по формуле
         1/(x**y) '''

    y = abs(y)
    tmp_x = x
    inx = y

    while inx > 1:
        x *= tmp_x
        inx -= 1

    return 1 / x


x_num = get_x_num()
y_num = get_y_num()

print(f"\n(**)    решение: {x_num} ^ {y_num} = {my_func(x_num, y_num)}")
print(f"\n(cicle) решение: {x_num} ^ {y_num} = {my_func_2(x_num, y_num)}")
