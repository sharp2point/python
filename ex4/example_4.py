# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы:
# go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
import time


class Car:
    _speed = 0
    _max_speed = 250
    _acc = 0  # ускорение
    _color = ""
    _name = ""
    _is_police = False
    _dir_side = "s"  # s - прямо l - лево r - право

    def __init__(self, name, color):
        self._name = name
        self._color = color

    @property
    def name(self):
        return self._name

    @property
    def dir_side(self):
        return self._dir_side

    def set_acc(self, val):
        self._acc = val

    def go(self):
        if self._speed < self._max_speed:
            self._speed += self._acc
        else:
            self._speed = self._max_speed

    def stop(self):
        if self._speed > 0:
            self._speed -= (self._acc * 2)
        else:
            self._speed = 0

    def turn_direction(self, dir_side: str):
        self._dir_side = dir_side
        if dir_side == "w":
            return "Едем прямо "
        elif dir_side == "x":
            return "Тормозим "
        elif dir_side == "l":
            return "Поворот на лево "
        elif dir_side == "r":
            return "Поворот на право "

    def show_speed(self):
        if self._speed == self._max_speed:
            return "max"
        elif self._speed == 0:
            return "stop"
        return self._speed

    def __str__(self):
        return f"{self.__class__}:   {self._name},   color: {self._color},   max_speed: {self._max_speed}   " \
               f"police: {self._is_police}"


# -----------------------------------------------------------

class TownCar(Car):
    _max_speed = 60

    def __init__(self, name="TownCar", color="black"):
        super().__init__(name, color)


class SportCar(Car):

    def __init__(self, name="SportCar", color="black"):
        super().__init__(name, color)


class WorkCar(Car):
    _max_speed = 40

    def __init__(self, name="WorkCar", color="black"):
        super().__init__(name, color)


class PoliceCar(Car):
    _is_police = True

    def __init__(self, name="PoliceCar", color="black"):
        super().__init__(name, color)


# ---------------Инициаизация объектов-------------------------------------
auto_list = []

town_car = TownCar("Paz", "white")
town_car.set_acc(1)
auto_list.append(town_car)

sport_car = SportCar("Porshe", "red")
sport_car.set_acc(5)
auto_list.append(sport_car)

work_car = WorkCar("Kamaz", "yellow")
work_car.set_acc(2)
auto_list.append(work_car)

police_car = PoliceCar("Priora", "blue")
police_car.set_acc(4)
auto_list.append(police_car)

# ----------------Рабочий цикл---------------------------

input_pos_auto = int(input(f"Выберите авто,введите целое от 0 до {len(auto_list) - 1}:"))
auto_search = auto_list[input_pos_auto]
print(f"Вы выбрали: {auto_search}")
print("*-" * 30)
# input_dir_side = input("Чтобы повернуть нажмите <l> - лево, <r> - право, <s> - прямо: ")
# auto_search.turn_direction(input_dir_side)


input("Для начала поездки нажмите ENTER")
while_cnt = 0
while True:
    view_str = ""
    # Каждые 5 проходов спрашиваем поьзователя
    if while_cnt % 5 == 0:
        input_dir_side = input("Чтобы повернуть нажмите <e> - выйти из программы"\
                               " <w> - прямо, <l> - лево, <r> - право, <x> - стоп: ")
        if input_dir_side == "w":
            view_str += auto_search.turn_direction("w")
        elif input_dir_side == "x":
            view_str += auto_search.turn_direction("x")
        elif input_dir_side == "l":
            view_str += auto_search.turn_direction("l")
        elif input_dir_side == "r":
            view_str += auto_search.turn_direction("r")
        elif input_dir_side == "e":
            break;


    # если нажали W - набираем скорость до MAX , если X - тормозим до 0
    if auto_search.dir_side == "w":
        auto_search.go()
    elif auto_search.dir_side == "x":
        auto_search.stop()

    # вывод на печать представление
    view_str += (f"*{auto_search.name}: {auto_search.show_speed()}*")
    print(view_str)

    time.sleep(0.1)
    while_cnt += 1

print("*-"*30)
print("Программа завершена, жертв нет !")
