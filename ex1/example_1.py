# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку
# конструктора класса (метод __init__()), который должен принимать
# данные (список списков) для формирования матрицы.
from functools import reduce


class MatrixExcept(Exception):
    def __init__(self, err_str):
        self.txt = "MatrixException: " + err_str


class Matrix:

    def __init__(self, matrix_list=[[1, 0], [0, 1]]):
        self._matrix = matrix_list
        self._m_lines = len(matrix_list)  # кличество строк
        self._m_rows = len(matrix_list[0])  # количество столбцов
        self._m_name = "M"  # название матрицы

    m_name = property()

    @m_name.setter
    def m_name(self, val):
        self._m_name = val

    @m_name.getter
    def m_name(self):
        return self._m_name

    @property
    def matrix(self):
        return self._matrix

    @property
    def m_rows(self):
        return self._m_rows

    @property
    def m_lines(self):
        return self._m_lines

    def _verify_matrix(self, matrix):
        """
        Метод сравнивает размерность матриц
        :param matrix: Матрица для операции __add__
        :return: если размеры матриц разные False иначе True
        """
        try:
            if self._m_rows != matrix.m_rows or self._m_lines != matrix.m_lines:
                raise MatrixExcept(f"\033[31m Размер матриц не совпадает \033[30m")
        except MatrixExcept as me:
            print(me)
            return False
        return True

    def __add__(self, matrix):
        if self._verify_matrix(matrix):
            sum_matrix = []

            for i in range(self._m_lines):
                new_matrix_line = []
                for j in range(self._m_rows):
                    num_ij = self._matrix[i][j] + matrix.matrix[i][j]
                    new_matrix_line.append(num_ij)
                sum_matrix.append(new_matrix_line)

            return Matrix(sum_matrix)
        else:
            return f"\033[31m Error ! Matrix append\033[30m"

    def __str__(self):
        present_str = ""
        for i in range(self._m_lines):
            line_str = ""
            for j in range(self._m_rows):
                line_str += f"{self._matrix[i][j]: 4}"

            present_str += f"{line_str}\n"

        return present_str


# пример испоьзования класса Matrix
# --------------- Matrix 3x3 ----------------------
m1_33 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
m2_33 = Matrix([[10, 1, 0], [0, 10, 1], [1, 0, 10]])
m3_33 = Matrix([[5, 10, 1], [1, 5, 10], [10, 1, 5]])

msum_33 = m1_33 + m2_33 + m3_33
print("*-" * 30)
print("Результат сложения матриц 3x3: \n")
print(msum_33)

# ----------------Matrix 3x2 ------------------------
m1_32 = Matrix([[1, 0, 0], [0, 1, 0]])
m2_32 = Matrix([[5, 1, 0], [0, 5, 1]])
m3_32 = Matrix([[7, 10, 1], [1, 7, 10]])

msum_32 = m1_32 + m2_32 + m3_32
print("*-" * 30)
print("\nРезультат сложения матриц 3x2: \n")
print(msum_32)
print("*-" * 30)
# ----------------- Обработка ошибочной ситуации (не совпадают размеры матриц)--------------------------
m1_32 = Matrix([[1, 0, 0], [0, 1, 0]])
m2_22 = Matrix([[5, 1], [0, 5]])

print("Ошибка размеров матриц:\n")
msum = m1_32 + m2_22
