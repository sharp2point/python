# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
# параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
from abc import ABC, abstractmethod


class Clothes(ABC):
    """
    Абстрактный класс одежды
    """

    @property
    def amount_fabric(self):
        pass

    @abstractmethod
    def _amount_fabric_calc(self):
        """
        Расчет расхода ткани
        :return:
        """
        pass


class Coat(Clothes):
    """
    Класс Пальто
    """

    def __init__(self, c_size=1):
        self._c_size = c_size
        self._amount_fabric = 0

    def _amount_fabric_calc(self):
        self._amount_fabric = self._c_size / 6.5 + 0.5
        return self._amount_fabric

    amount_fabric = property()
    c_size = property()

    @amount_fabric.getter
    def amount_fabric(self):
        return self._amount_fabric_calc()

    @c_size.setter
    def c_size(self, val):
        self._c_size = val

    @c_size.getter
    def c_size(self):
        return self._c_size

    def __str__(self):
        return f"Расход материала на ПАЛЬТО {self.c_size} размера : {self.amount_fabric:.3} м.пог"


class Costume(Clothes):
    """
    Класс Пальто
    """

    def __init__(self, c_size=1):
        self._c_size = c_size
        self._amount_fabric = 0

    def _amount_fabric_calc(self):
        self._amount_fabric = self._c_size * 2 + 0.3
        return self._amount_fabric

    amount_fabric = property()
    c_size = property()

    @amount_fabric.getter
    def amount_fabric(self):
        return self._amount_fabric_calc()

    @c_size.setter
    def c_size(self, val):
        self._c_size = val

    @c_size.getter
    def c_size(self):
        return self._c_size

    def __str__(self):
        return f"Расход материала на КОСТЮМ роста {self.c_size}м.  : {self.amount_fabric:.3} м.пог"


# ------------------- Пример использования классов --------------------------------------------
# -------------- Coat -----------------------------------
coat = Coat(32)
print(coat)

coat.c_size = 34 # меняем размер
# печать с помощью свойств класса
print(f"Размер ПАЛЬТО изменён на {coat.c_size} : расход {coat.amount_fabric:.3} м.пог")
print("*-" * 30)

# -------------- Costume -----------------------------------
costume = Costume(1.8)
print(costume)

costume.c_size = 1.9 # меняем размер
# печать с помощью свойств класса
print(f"Рост КОСТЮМА изменён на {costume.c_size}м. : расход {costume.amount_fabric:.3} м.пог")
print("*-" * 30)
