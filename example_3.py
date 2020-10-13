#Реализовать функцию my_func(), которая принимает
# три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

input_lst = input("Введите три значения через пробел:").split()

def sum_3max(num_1, num_2,num_3):
    min_num = min(num_1,num_2,num_3)
    return sum([num_1,num_2,num_3]) - min_num

sum_max = sum_3max(*(list(map(float,input_lst))))
print(f"Сумма двух максимаьных:{sum_max}")
