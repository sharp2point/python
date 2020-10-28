# 7.7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел.


class ComplexNumb:
    """
    Класс комплексных чисел
    """
    def __init__(self, real_prt=1, imgn_prt=1):
        self._real_prt, self._imgn_prt = real_prt, imgn_prt

    def __add__(self, other):
        return ComplexNumb(self._real_prt + other._real_prt, self._imgn_prt + other._imgn_prt)

    def __mul__(self, other):
        a1 = self._real_prt
        a2 = other._real_prt
        b1 = self._imgn_prt
        b2 = other._imgn_prt

        return ComplexNumb((a1 * a2 - b1 * b2), (a1 * b2 + a2 * b1))

    def __str__(self):
        if self._imgn_prt < 0:
            return f"{self._real_prt}{self._imgn_prt}i"
        else:
            return f"{self._real_prt}+{self._imgn_prt}i"

    @property
    def real(self):
        """
        Свойство возвращает реальную часть комексного числа
        :return:
        """
        return self._real_prt

    @property
    def imgn(self):
        """
        Свойство возвращает мнимую часть комплексного числа
        :return:
        """
        return self._imgn_prt


# --------------- Использование касса ComplexNumb -------------------------

print("реализация ComplexNum:")
cmpx = ComplexNumb(-1, -2)
cmpx2 = ComplexNumb(3, 4)
cmpx_sum = cmpx + cmpx2
cmpx_mul = cmpx * cmpx2
print(f"({cmpx}) + ({cmpx2}) = ({cmpx_sum})")
print(f"({cmpx}) * ({cmpx2}) = ({cmpx_mul})")

print("\nпроверка Built-in complex python:")
print(f"(-1-2j) + (3+4j) = {(-1-2j)+(3+4j)}")
print(f"(-1-2j) * (3+4j) = {(-1-2j)*(3+4j)}")
