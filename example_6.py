# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой.

input_str = input("Вводите слова через пробел:")


def title_word(word: str) -> str:
    '''
    Функция преобразования строки
    :param word: Слово
    :return: Преобразованное слово
    '''
    return word.title()


def transform_str(input_str: str, func_tranform) -> str:
    '''
    Функция преобразования строки
    :param input_str: Строка ввода
    :param func_tranform: функция преобразования
    :return: Преобразованная строка ввода
    '''
    return ' '.join(list(map(func_tranform, input_str.split())))


print(transform_str("hello my darlig", title_word))
