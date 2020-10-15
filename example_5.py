# 5. Реализовать формирование списка, используя функцию range() и
# возможности генератора. В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.

from functools import reduce

# генератор списка четных чисел от 100 до 1000
end_list = [i for i in range(100, 1000) if i % 2 == 0]
# print(end_list)

# результат умножения ченов списка end_list
multiply_num = reduce(lambda x, y: x * y, end_list)
print(f"Результат умножения: {multiply_num}")
