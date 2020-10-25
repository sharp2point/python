# 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
class CellSubException(Exception):

    def __init__(self, exc_str: str):
        self.text = "CellSubException: " + exc_str


class Cell:
    _world_cell = []

    def __init__(self, cell=1):
        self._cell_num = cell
        self.id = len(Cell._world_cell)
        Cell._world_cell.append(self)

    @classmethod
    def make_order(cls,cell,cnt_cell):
        star_cnt = cell.cell_num // cnt_cell
        star_fin = cell.cell_num % cnt_cell
        format_str = ""
        for i in range(star_cnt):
            format_str += f"{'*'*cnt_cell}\\n"
        format_str += f"{'*'*star_fin}"
        return format_str

    world_cell = property()

    @classmethod
    @world_cell.getter
    def world_cell(cls):
        return cls._world_cell

    cell_num = property()

    @cell_num.getter
    def cell_num(self):
        return self._cell_num

    def __add__(self, cell):
        return Cell(self.cell_num + cell.cell_num)

    def __sub__(self, cell):
        try:
            if (self.cell_num - cell.cell_num) < 0:
                raise CellSubException("Ошибка вычитания")
        except CellSubException as ex:
            print(ex)
            return -1
        return Cell(self.cell_num - cell.cell_num)

    def __mul__(self, cell):
        return Cell(self.cell_num * cell.cell_num)

    def __truediv__(self, cell):
        return Cell(self.cell_num // cell.cell_num)

    def __str__(self):
        return f"Cell id{self.id}:({self.cell_num})"


# Пример использования касса Cell

cell_1 = Cell(2)
cell_2 = Cell(5)
cell_3 = Cell(15)

print("*- Add -" * 10)
print(f"\033[31m Сложение:\033[30m\n\t{cell_1} + {cell_2} + {cell_3} = {cell_1 + cell_2 + cell_3}")
print(f"\033[34m В системе создано: {len(Cell.world_cell)} клеток\033[30m\n")

print("*- Sub -" * 10)
print(f"\033[31m Вычитание:\033[30m\n\t{cell_3} - {cell_2} - {cell_1} = {cell_3 - cell_2 - cell_1}")
print(f"\033[34m В системе создано: {len(Cell.world_cell)} клеток\033[30m\n")

print("*- Mul -" * 10)
print(f"\033[31m Умножение:\033[30m\n\t{cell_3} * {cell_2} * {cell_1} = {cell_3 * cell_2 * cell_1}")
print(f"\033[34m В системе создано: {len(Cell.world_cell)} клеток\033[30m\n")

print("*- Div -" * 10)
print(f"\033[31m Деление:\033[30m\n\t{cell_3} / {cell_2} / {cell_1} = {cell_3 / cell_2 / cell_1}")
print(f"\033[34m В системе создано: {len(Cell.world_cell)} клеток\033[30m\n")

# ------------- Обработка исключения при вычитании -------------------------------------
print("*- CellSubException -" * 10)
cell_m = Cell(10)
cell_v = Cell(11)
cell_sub = cell_m - cell_v

# ---------------- make_order() --------------------------------------------------------

print("*- Make_order 3 -" * 10)

# Make Order 3
for cell in Cell.world_cell:
    print(f"{cell}:\t {Cell.make_order(cell, 3)}")

print("*- Make_order 5 -" * 10)
# Make Order 5
for cell in Cell.world_cell:
    print(f"{cell}:\t {Cell.make_order(cell, 5)}")
