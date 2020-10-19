#1. Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

from io import open

with open("test.txt","w",encoding="utf-8") as file_handler:
    while True:
        input_str = input("Введите строку: ")
        if len(input_str) == 0:
            print("Программа завершена !")
            break
        else:
            file_handler.write(input_str + "\n")



