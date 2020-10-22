# 3. Реализовать базовый класс Worker (работник),
# в котором определить атрибуты: name, surname, position (должность), income (доход).

class Worker:
    name = ""
    soname = ""
    position = ""
    _income = {"wage": 0, "bonus": 0}

    def set_wage(self, val):
        self._income["wage"] = val

    def set_bonus(self, val):
        self._income["bonus"] = val


class Position(Worker):
    def __init__(self, name="John", soname="Snow"):
        self.name = name
        self.soname = soname

    def get_full_name(self):
        return f"{self.name} {self.soname}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


# -------------------------------------------------
pos = Position("Гамлет","Перцхалава")
pos.set_wage(900)
pos.set_bonus(90)
print(f"Доход {pos.get_full_name()} = {pos.get_total_income()}")
print("*-"*30)
# интерактивный режим
print("\n Задайте атрибуты рабочего")
input_name = input("Введите имя:")
input_soname = input("Введите фамилию:")
input_wage = float(input("Введите оклад рабочего:"))
input_bonus = float(input("Введите премию рабочего:"))

pos2 = Position(input_name,input_soname)
pos2.set_wage(input_wage)
pos2.set_bonus(input_bonus)

print("*-"*30)
print(f"Доход {pos2.get_full_name()} = {pos2.get_total_income()}")


