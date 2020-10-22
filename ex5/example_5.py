# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер)

class Stationery:
    _title = "undefined"

    def __init__(self, title: str):
        self._title = title

    def draw(self):
        return "Запуск отрисовки"


class Pen(Stationery):
    _color = ""

    def __init__(self, color="green"):
        super().__init__(title="Pen")
        self._color = color

    def draw(self):
        return f"I'm Draw {self._color} {self._title}"


class Pencil(Stationery):
    _color = ""

    def __init__(self, color="blue"):
        super().__init__(title="Pencil")
        self._color = color

    def draw(self):
        return f"I'm Draw {self._color} {self._title}"


class Handle(Stationery):
    _color = ""

    def __init__(self, color="red"):
        super().__init__(title="Handle")
        self._color = color

    def draw(self):
        return f"I'm Draw {self._color} {self._title}"


# ---------- Work  -----------------------------

pen = Pen("red")
print(pen.draw())

pencil = Pencil("black")
print(pencil.draw())

handle = Handle("fucsia")
print(handle.draw())
