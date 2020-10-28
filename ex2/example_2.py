# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
# параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
from abc import ABC, abstractmethod,  abstractproperty


class Clothes(ABC):
    """
    Абстрактный класс одежды
    """
    @abstractmethod
    def fabric_all_calc(cls):
        """
        Подсчитывает материал на всю одежду объектов касса
        :param cloth:
        :return:
        """
        pass

    @abstractmethod
    def _amount_fabric_calc(self):
        """
        Расчет расхода ткани
        :return:
        """
        pass

    @property
    def amount_fabric(self):
        pass

    @property
    def c_size(self):
        pass


class Coat(Clothes):
    """
    Класс Пальто
    """
    _fabric_all = list()

    def __init__(self, c_size=1):
        self._c_size = c_size
        self._amount_fabric = 0
        Coat._fabric_all.append(self)

    @classmethod
    def fabric_all_calc(cls):
        sum_all = 0
        for i in cls._fabric_all:
            sum_all += i.amount_fabric

        return len(cls._fabric_all),sum_all

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
    _fabric_all = list()

    def __init__(self, c_size=1):
        self._c_size = c_size
        self._amount_fabric = 0
        Costume._fabric_all.append(self)

    @classmethod
    def fabric_all_calc(cls):
        sum_all = 0
        for i in cls._fabric_all:
            sum_all += i.amount_fabric

        return len(cls._fabric_all),sum_all

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

coat.c_size = 34  # меняем размер
# печать с помощью свойств класса
print(f"Размер ПАЛЬТО изменён на {coat.c_size} : расход {coat.amount_fabric:.3} м.пог")
print("*-" * 30)

# -------------- Costume -----------------------------------
costume = Costume(1.8)
print(costume)

costume.c_size = 1.9  # меняем размер
# печать с помощью свойств класса
print(f"Рост КОСТЮМА изменён на {costume.c_size}м. : расход {costume.amount_fabric:.3} м.пог")
print("*-" * 30)

# ------------------Подсчет общего расхода материала----------------------------
costume_1 = Costume(2.2)
costume_2 = Costume(1.9)
costume_3 = Costume(1.1)
costume_4 = Costume(0.8)

coat_1 = Coat(32)
coat_2 = Coat(20)
coat_3 = Coat(43)

print("Подсчет общего расхода материала:")

costume_fabric = Costume.fabric_all_calc()
print(f"\tНа {costume_fabric[0]} костюма ушло: {costume_fabric[1]:.3} м.пог материала")

coat_fabric = Coat.fabric_all_calc()
print(f"\tНа {coat_fabric[0]} пальто ушло: {coat_fabric[1]:.3} м.пог материала")

cloth_cnt = coat_fabric[0] + costume_fabric[0]
fabric_all = coat_fabric[1] + costume_fabric[1]
print(f"Суммарный расход материала на {cloth_cnt} изделия: {fabric_all:.3} м.пог")

