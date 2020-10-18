# 4.Необходимо написать программу, открывающую файл на чтение и считывающую
# построчно данные. При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

from io import open

translate_dict = {
    "one": "один",
    "two": "два",
    "three": "три",
    "four": "четыре"
}


def translate_str(input_str: str) -> str:
    """
    функция переводит входную строку
    :param input_str: строка
    :return: переведенная строка
    """
    tmp_str = input_str.lower()
    lst = tmp_str.split()
    lst[0] = translate_dict.get(lst[0])
    return " ".join(lst) + "\n"


def create_translate_file(file_name: str, input_str: str):
    """
    Функция построчно записывает данные в файл перевода
    :param file_name: Имя файла, строка
    :param input_str:
    :return:
    """

    with open(file_name, "a", encoding="utf-8") as file_handl:
        file_handl.write(input_str)


def read_file(file_name: str):
    t_file_name = f"t_{file_name}"
    with open(t_file_name, "w", encoding="utf-8") as file_handl:
        pass  # подготовить/очистить файл перевода
    with open(file_name, "r", encoding="utf-8") as file_handl:
        for i in file_handl:
            t_str = translate_str(i)
            create_translate_file(t_file_name, t_str)


# ---------------- Work --------------------------
read_file("test.txt")
print("Перевод окончен !")
