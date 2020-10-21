# 1. Создать класс TrafficLight (светофор) и определить
# у него один атрибут color (цвет) и метод running (запуск).

import os
import time
from itertools import cycle

# словарь конфигурации
config_traf = {
    "Красный": '\033[1;31m',
    "Желтый": '\033[1;33m',
    "Зеленый": '\033[1;32m',
    "default": '\033[1;30m'
}


class ColorLamp:
    """
    Класс ламп
    __is_lighting - поле опредеяет включена или выключена лампа
        get_is_lighting - метод get для поля __is_lighting
        set_is_lighting(bool) - метод set для поля __is_lighting
    __color_lamp - переменная цвета лампы
        get_color - метод get для переменной __color_lamp

    draw_me(config_dict) - метод отрисовки экземпляра класса
    --------------------------------------------------------------
    пример использования:
        lamp = ColorLamp(color) по умолчанию выключена
    """
    __is_lighting = False  # поле включение лампы
    __color_lamp = ""  # поле цвета лампы

    def __init__(self, color_lamp: str):
        self.__color_lamp = color_lamp

    # def __str__(self):
    #     return f"I'm Color Lamp {self.__color_lamp}!"

    def get_color(self):
        return self.__color_lamp

    def get_is_lighting(self):
        return self.__is_lighting

    def set_is_lighting(self, is_val: bool):
        self.__is_lighting = is_val

    def draw_me(self, config_trf: dict):
        if self.__is_lighting:
            __conf = config_trf.get(self.__color_lamp)
        else:
            __conf = config_trf.get("default")
        out_str = f" {__conf} {self.__color_lamp} "
        return out_str


class TrafficLight:
    """
     Класс светофора
     __color - # список [[лампа,время],....]
        append_lamp(ColorLamp,delay) - подключает лампу ColorLamp и устанавивает время задержки delay
        get_len_color - возвращает количество элементов списка __color
    swith_lamp(pos) - логика перекючения ламп
    draw_me() - отрисовка работы класса
    """
    __color = []

    def append_lamp(self, color_lamp: ColorLamp, delay_time: int):
        for lamp in self.__color:
            if color_lamp.get_color() == lamp[0].get_color():
                print("Такая лампа уже есть !")
        else:
            self.__color.append([color_lamp, delay_time])

    def get_len_color(self):
        return len(self.__color) - 1

    def switch_lamp(self, pos_light: int) -> int:
        for lamp in self.__color:
            lamp[0].set_is_lighting(False)
        self.__color[pos_light][0].set_is_lighting(True)
        return self.__color[pos_light][1]

    def draw_me(self):
        __present_str = ""
        for lamp in self.__color:
            __present_str += lamp[0].draw_me(config_traf)
        __present_str += '\033[1;30m'
        return __present_str


# ---------- Work Cycle ------------------------------

red_lamp = ColorLamp("Красный")
ylw_lamp = ColorLamp("Желтый")
grn_lamp = ColorLamp("Зеленый")

traf = TrafficLight()
traf.append_lamp(red_lamp, 7)
traf.append_lamp(ylw_lamp, 3)
traf.append_lamp(grn_lamp, 2)

input("Для запуска программы нажмите ENTER")
switch_cnt = 0
while_cnt = 50

while while_cnt:
    delay_time = traf.switch_lamp(switch_cnt)
    print(traf.draw_me())
    switch_cnt += 1
    if switch_cnt > traf.get_len_color():
        switch_cnt = 0
    print("Осталось")
    while delay_time:
        time.sleep(1)
        print(f"   {delay_time} сек.")
        delay_time -= 1
    print("Переключение")
    while_cnt -= 1

print("Программа завершена !")
