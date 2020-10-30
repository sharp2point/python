# 4.5.6 Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников.

from OfficeEquipStorage import OfficeEquipStorage
from OfficeEquipFabric import OfficeEquipFabric

# ---------------------------------------------------------------

storage_EQ = OfficeEquipStorage()

fabric_EQ = OfficeEquipFabric()

for i in range(5):  # наполнение склада
    scaner = fabric_EQ.create_eq_rnd("scaner", storage_EQ)
    copyer = fabric_EQ.create_eq_rnd("copyer", storage_EQ)
    printer = fabric_EQ.create_eq_rnd("printer", storage_EQ)

# ------------------обработка Пользовательского ввода ---------------------------
print("Команда <set> пошагово создает новое устройство на складе.\n")
print("Комманда <get> <printer | scaner | copyer | all | id> запрашивает склад")
print("Например: комманда <get all> выведет на печать все товары на складе.")
print("Комманда <get 1001> выведет на печать и добавит в корзину товар с id = 1001.\n")


# ------------ Work Cycle ------------------------------------
you_basket = list()  # корзина покупок

while True:
    eq, basket = storage_EQ.request_storage_EQ()
    if basket and eq:
        you_basket.append(eq)
    else:
        print(f"\t{eq}\n")

    print(f"В вашей корзине {len(you_basket)} заказов:")
    for i in you_basket:
        print(i)
