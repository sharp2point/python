# 2. Реализовать класс Road (дорога), в котором определить  атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.

class Road:

    def __init__(self, length=1, width=1):
        self._length = length
        self._width = width

    def set_length(self, val):
        """
        Свойство set динны дороги
        :param val:
        :return:
        """
        self._length = val

    def set_width(self, val):
        """
        Свойство set ширины дороги
        :param val:
        :return:
        """
        self._width = val

    def sqare_calc(self):
        """
        Расчет площади дорожного полотна
        :return: площадь дорожного полотна
        """
        return self._length * self._width

    def weight_calc(self, weight=1, thick=1):
        """
        :param weight: вес 1м.кв покрытия
        :param thick: тощина покрытия
        :return: вес дорожного порытия
        """
        return self.sqare_calc() * weight * thick


# --------  Work  ---------------------
road_asph = Road(length=5000,width=20)
road_weight = road_asph.weight_calc(weight=25,thick=5)
print(f"Вес доожного покрытия {float(road_weight) : .3}")


# Интеррактивный режим
input_length = float(input("Введите длинну дороги:"))
road_asph.set_length(input_length)

input_width = float(input("Введите ширину дороги:"))
road_asph.set_width(input_width)

input_weight = float(input("Введите вес 1см покрытия:"))
input_thick = float(input("Введите толщину слоя покрытия:"))
road_weight = road_asph.weight_calc(weight=input_weight, thick=input_thick)

print(f"Вес доожного покрытия {float(road_weight) : .3}")
