#2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

from io import open

with open("test.txt","r",encoding="utf-8") as file_handl:
    line_cnt = 0
    word_cnt = 0
    for i in file_handl:
        line_cnt += 1
        world_lst = i.split()
        for j in world_lst:
            word_cnt += 1
        print(i)
        print(f"В строке N{line_cnt}: {word_cnt} слов.")
        print("*- "*30)
        word_cnt = 0
