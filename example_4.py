# разбиение строкового ввода
input_lst = input("Введите слова через пробел:").split(" ")

for i in enumerate(input_lst):
    if len(i[1]) < 10:
        print(f"{i[0]+1}.{i[1]}")
    else:
        print(f"{i[0] + 1}.{i[1][:10:]}")
