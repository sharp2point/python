# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def carry_dividend(dividend_num: float):
    def carry_divider(divider_num: float):
        return dividend_num / divider_num

    return carry_divider


dividend_num = float(input("Введите делимое число:"))
quotient_num = carry_dividend(dividend_num)

divider_num = float(input("Введите число делитель:"))
print(f"Результат деления {dividend_num}/{divider_num} = {quotient_num(divider_num):.2}")
